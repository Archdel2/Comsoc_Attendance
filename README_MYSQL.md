# COMSOC Attendance System - MySQL Version

This is the MySQL version of the COMSOC Attendance Management System, adapted to work with your existing `comsoc_attendance` database.

## Database Structure

The system is designed to work with the following MySQL tables:

### Students Table
- `student_id` (VARCHAR(20)) - Primary key, also used as QR code data
- `fname` (VARCHAR(50)) - Student's first name
- `year_level` (VARCHAR(20)) - Student's year level
- `course` (VARCHAR(50)) - Student's course
- `created_at` (TIMESTAMP) - When the record was created

### Events Table
- `event_id` (INT) - Auto-increment primary key
- `event_name` (VARCHAR(100)) - Name of the event
- `event_date` (DATE) - Date of the event
- `created_at` (TIMESTAMP) - When the record was created

### AttendanceRecords Table
- `record_id` (INT) - Auto-increment primary key
- `record_name` (VARCHAR(100)) - Name of the attendance record
- `event_id` (INT) - Foreign key to Events table
- `created_at` (TIMESTAMP) - When the record was created

### Attendance Table
- `attendance_id` (INT) - Auto-increment primary key
- `record_id` (INT) - Foreign key to AttendanceRecords table
- `student_id` (VARCHAR(20)) - Foreign key to Students table
- `student_fname` (VARCHAR(50)) - Student's first name (denormalized)
- `student_year_level` (VARCHAR(20)) - Student's year level (denormalized)
- `student_course` (VARCHAR(50)) - Student's course (denormalized)
- `status` (ENUM) - 'Present', 'Absent', or 'Excused'
- `timestamp` (TIMESTAMP) - When attendance was marked
- Unique constraint on (record_id, student_id)

## Setup Instructions

### 1. Prerequisites
- MySQL Server running
- Python 3.7+
- Database `comsoc_attendance` already created

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Edit the `.env` file with your MySQL credentials:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=comsoc_attendance
DB_USER=root
DB_PASSWORD=your_password_here
```

### 4. Test Database Connection
```bash
python test_db_connection.py
```

### 5. Run the Application
```bash
python run.py
```

## Features

- **Student Management**: Add, view, and manage student records
- **Event Management**: Create and manage events
- **Attendance Tracking**: Mark attendance with Present/Absent/Excused status
- **QR Code Scanning**: Scan student QR codes to mark attendance
- **Data Export**: Import students from CSV files
- **Real-time Updates**: Live attendance status updates

## Usage

### Adding Students
1. Navigate to Masterlist page
2. Students can be imported from CSV or added manually
3. CSV format: `student_id,fname,year_level,course`

### Creating Events
1. Navigate to Events page
2. Enter event name and click "Add New Event"
3. System automatically creates attendance records for all students

### Taking Attendance
1. Select an event from the Events page
2. Use the attendance table to mark status manually
3. Or use QR code scanner for automatic attendance marking

### QR Code Scanning
1. Navigate to an event's attendance page
2. Click "Check Attendance (Scan QR)"
3. Point camera at student QR codes
4. Students are automatically marked as Present

## Troubleshooting

### Common Issues

1. **Connection Error**: Check MySQL server is running and credentials are correct
2. **Table Not Found**: Run `test_db_connection.py` to create tables
3. **Permission Denied**: Ensure MySQL user has proper permissions on the database
4. **Camera Not Working**: Check camera permissions and device availability

### Database Permissions
Your MySQL user needs these permissions on `comsoc_attendance`:
```sql
GRANT ALL PRIVILEGES ON comsoc_attendance.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```

## File Structure

- `main_app.py` - Main application logic
- `database.py` - MySQL database operations
- `ui_pages.py` - User interface components
- `camera_scanner.py` - QR code scanning functionality
- `config.py` - Configuration and environment variables
- `run.py` - Application launcher
- `test_db_connection.py` - Database connection tester
- `.env` - Environment configuration
- `requirements.txt` - Python dependencies

## Migration from SQLite

If you're migrating from the SQLite version:
1. Export your existing data
2. Create the MySQL database structure
3. Import data into the new MySQL tables
4. Update the `.env` file with MySQL credentials
5. Test the connection and run the application

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify database connection with test script
3. Check MySQL error logs
4. Ensure all dependencies are installed correctly
