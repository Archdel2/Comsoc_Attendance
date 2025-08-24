#!/usr/bin/env python3
"""
Script to view database contents
"""

import sys
import os

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from database import DatabaseManager
    
    print("🔍 COMSOC Attendance Database Viewer")
    print("=" * 50)
    
    # Connect to database
    db = DatabaseManager()
    
    # View Students
    print("\n📚 STUDENTS TABLE:")
    print("-" * 30)
    students = db.get_all_students()
    if students:
        print(f"Total Students: {len(students)}")
        print("\nFirst 10 students:")
        for i, student in enumerate(students[:10], 1):
            print(f"{i:2}. ID: {student['student_id']:<12} | Name: {student['fname']:<20} | Year: {student['year_level']:<10} | Course: {student['course']}")
        if len(students) > 10:
            print(f"... and {len(students) - 10} more students")
    else:
        print("No students found")
    
    # View Events
    print("\n📅 EVENTS TABLE:")
    print("-" * 30)
    events = db.get_all_events()
    if events:
        print(f"Total Events: {len(events)}")
        for event in events:
            print(f"ID: {event['event_id']} | Name: {event['event_name']} | Date: {event['event_date']}")
    else:
        print("No events found")
    
    # View Attendance Records
    print("\n📊 ATTENDANCE RECORDS TABLE:")
    print("-" * 30)
    try:
        with db.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM AttendanceRecords LIMIT 5")
            records = cursor.fetchall()
            if records:
                print(f"Total Records: {len(records)} (showing first 5)")
                for record in records:
                    print(f"ID: {record['record_id']} | Name: {record['record_name']} | Event ID: {record['event_id']}")
            else:
                print("No attendance records found")
    except Exception as e:
        print(f"Could not read attendance records: {e}")
    
    # View Sample Attendance Data
    print("\n✅ SAMPLE ATTENDANCE DATA:")
    print("-" * 30)
    if events:
        first_event = events[0]
        attendance = db.get_attendance_for_event(first_event['event_id'])
        if attendance:
            print(f"Attendance for Event: {first_event['event_name']}")
            print(f"Total Records: {len(attendance)} (showing first 5)")
            for i, record in enumerate(attendance[:5], 1):
                print(f"{i}. {record['student_fname']} ({record['student_id']}) - {record['status']}")
        else:
            print("No attendance data found for this event")
    
    # Close connection
    db.close()
    
    print("\n" + "=" * 50)
    print("💡 To add events and see more data, run the main application:")
    print("   python run.py")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
