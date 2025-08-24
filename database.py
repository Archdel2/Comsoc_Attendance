"""
Database management module for the Attendance Management System
"""

import pymysql
import csv
from datetime import datetime
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, SAMPLE_STUDENTS


class DatabaseManager:
    """Handles all database operations for the attendance system"""
    
    def __init__(self):
        """Initialize database connection"""
        try:
            self.conn = pymysql.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                autocommit=True,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print(f"Connected to MySQL database: {DB_NAME}")
        except pymysql.Error as err:
            print(f"Error connecting to MySQL: {err}")
            raise
    
    def create_tables(self):
        """Create necessary database tables if they don't exist"""
        try:
            with self.conn.cursor() as cursor:
                # Students table
                cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                    student_id VARCHAR(20) PRIMARY KEY,
                    fname VARCHAR(50) NOT NULL,
                    year_level VARCHAR(20) NOT NULL,
                    course VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
                
                # Events table
                cursor.execute('''CREATE TABLE IF NOT EXISTS Events (
                    event_id INT AUTO_INCREMENT PRIMARY KEY,
                    event_name VARCHAR(100) NOT NULL,
                    event_date DATE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
                
                # Attendance Records table
                cursor.execute('''CREATE TABLE IF NOT EXISTS AttendanceRecords (
                    record_id INT AUTO_INCREMENT PRIMARY KEY,
                    record_name VARCHAR(100) NOT NULL,
                    event_id INT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE
                )''')
                
                # Attendance table
                cursor.execute('''CREATE TABLE IF NOT EXISTS Attendance (
                    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
                    record_id INT NOT NULL,
                    student_id VARCHAR(20) NOT NULL,
                    student_fname VARCHAR(50) NOT NULL,
                    student_year_level VARCHAR(20) NOT NULL,
                    student_course VARCHAR(50) NOT NULL,
                    status ENUM('Present', 'Absent', 'Excused') DEFAULT 'Absent',
                    timestamp TIMESTAMP NULL,
                    FOREIGN KEY (record_id) REFERENCES AttendanceRecords(record_id) ON DELETE CASCADE,
                    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
                    UNIQUE KEY unique_attendance (record_id, student_id)
                )''')
                
                self.conn.commit()
                print("Database tables created/verified successfully")
                
        except pymysql.Error as err:
            print(f"Error creating tables: {err}")
            raise
    
    def import_students_from_csv(self, filename):
        """Import students from a CSV file"""
        try:
            with self.conn.cursor() as cursor:
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    next(reader) 
                    for row in reader:
                        if len(row) >= 4:
                            cursor.execute(
                                "INSERT IGNORE INTO Students (student_id, fname, year_level, course) VALUES (%s, %s, %s, %s)", 
                                (row[0], row[1], row[2], row[3])
                            )
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Error importing CSV: {e}")
            return False
    
    def get_all_students(self):
        """Retrieve all students from the database"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT student_id, fname, year_level, course FROM Students")
                return cursor.fetchall()
        except pymysql.Error as err:
            print(f"Error fetching students: {err}")
            return []
    
    def get_all_events(self):
        """Retrieve all events from the database"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT event_id, event_name, event_date FROM Events")
                return cursor.fetchall()
        except pymysql.Error as err:
            print(f"Error fetching events: {err}")
            return []
    
    def create_event(self, name):
        """Create a new event"""
        try:
            date = datetime.now().date()
            with self.conn.cursor() as cursor:
                cursor.execute("INSERT INTO Events (event_name, event_date) VALUES (%s, %s)", (name, date))
                event_id = cursor.lastrowid
                self.conn.commit()
                return event_id
        except pymysql.Error as err:
            print(f"Error creating event: {err}")
            return None
    
    def create_attendance_record(self, record_name, event_id):
        """Create a new attendance record for an event and initialize all students as absent"""
        try:
            with self.conn.cursor() as cursor:
                # Create attendance record
                cursor.execute("INSERT INTO AttendanceRecords (record_name, event_id) VALUES (%s, %s)", (record_name, event_id))
                record_id = cursor.lastrowid
                
                # Initialize all students as absent for this record
                students = self.get_all_students()
                for student in students:
                    cursor.execute(
                        "INSERT INTO Attendance (record_id, student_id, student_fname, student_year_level, student_course, status) VALUES (%s, %s, %s, %s, %s, %s)",
                        (record_id, student['student_id'], student['fname'], student['year_level'], student['course'], 'Absent')
                    )
                
                self.conn.commit()
                return record_id
        except pymysql.Error as err:
            print(f"Error creating attendance record: {err}")
            return None
    
    def get_attendance_for_event(self, event_id):
        """Get attendance records for a specific event"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''SELECT a.student_id, a.student_fname, a.student_year_level, a.student_course, a.status, a.timestamp
                                  FROM Attendance a 
                                  JOIN AttendanceRecords ar ON a.record_id = ar.record_id 
                                  WHERE ar.event_id = %s''', (event_id,))
                return cursor.fetchall()
        except pymysql.Error as err:
            print(f"Error fetching attendance: {err}")
            return []
    
    def get_records_for_event(self, event_id):
        """Get all attendance records for a specific event"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''SELECT record_id, record_name, created_at
                                  FROM AttendanceRecords 
                                  WHERE event_id = %s''', (event_id,))
                return cursor.fetchall()
        except pymysql.Error as err:
            print(f"Error fetching records: {err}")
            return []
    
    def get_students_for_record(self, record_id):
        """Get all students and their attendance for a specific record"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''SELECT student_id, student_fname, student_year_level, student_course, status, timestamp
                                  FROM Attendance 
                                  WHERE record_id = %s''', (record_id,))
                return cursor.fetchall()
        except pymysql.Error as err:
            print(f"Error fetching students for record: {err}")
            return []
    
    def update_attendance_status(self, event_id, student_id, status):
        """Update attendance status for a specific student at a specific event"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''UPDATE Attendance a 
                                  JOIN AttendanceRecords ar ON a.record_id = ar.record_id 
                                  SET a.status = %s, a.timestamp = NOW()
                                  WHERE ar.event_id = %s AND a.student_id = %s''',
                               (status, event_id, student_id))
                self.conn.commit()
                return True
        except pymysql.Error as err:
            print(f"Error updating attendance: {err}")
            return False
    
    def mark_student_present(self, event_id, student_id):
        """Mark a student as present for a specific event"""
        return self.update_attendance_status(event_id, student_id, 'Present')
    
    def get_student_by_id(self, student_id):
        """Get student information by student ID"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT student_id, fname, year_level, course FROM Students WHERE student_id = %s", (student_id,))
                return cursor.fetchone()
        except pymysql.Error as err:
            print(f"Error fetching student: {err}")
            return None
    
    def add_student(self, student_id, fname, year_level, course):
        """Add a new student to the database"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Students (student_id, fname, year_level, course) VALUES (%s, %s, %s, %s)",
                    (student_id, fname, year_level, course)
                )
                self.conn.commit()
                return True
        except pymysql.Error as err:
            print(f"Error adding student: {err}")
            return False
    
    def import_sample_data(self):
        """Import sample student data for testing purposes"""
        try:
            with self.conn.cursor() as cursor:
                for student in SAMPLE_STUDENTS:
                    cursor.execute(
                        "INSERT IGNORE INTO Students (student_id, fname, year_level, course) VALUES (%s, %s, %s, %s)", 
                        student
                    )
                self.conn.commit()
                print("Sample data imported successfully")
        except pymysql.Error as err:
            print(f"Error importing sample data: {err}")
    
    def close(self):
        """Close the database connection"""
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
            print("Database connection closed")
