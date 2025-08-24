"""
Configuration file for the Attendance Management System
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_NAME = os.getenv('DB_NAME', 'comsoc_attendance')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')

# Application settings
APP_TITLE = os.getenv('APP_TITLE', "COMSOC Attendance Recorder")
APP_WIDTH = int(os.getenv('APP_WIDTH', 900))
APP_HEIGHT = int(os.getenv('APP_HEIGHT', 700))

# Camera settings
CAMERA_UPDATE_INTERVAL = int(os.getenv('CAMERA_UPDATE_INTERVAL', 30))  # milliseconds
CAMERA_DISPLAY_WIDTH = int(os.getenv('CAMERA_DISPLAY_WIDTH', 640))
CAMERA_DISPLAY_HEIGHT = int(os.getenv('CAMERA_DISPLAY_HEIGHT', 480))

# UI styling
BUTTON_STYLE = """
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 15px;
        font-size: 16px;
        border-radius: 5px;
        margin: 10px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
"""

# Sample data for testing
SAMPLE_STUDENTS = [
    ('2023-0001', 'John Doe', '1st Year', 'Computer Science'),
    ('2023-0002', 'Jane Smith', '2nd Year', 'Information Technology'),
    ('2023-0003', 'Robert Johnson', '3rd Year', 'Computer Engineering'),
    ('2023-0004', 'Emily Davis', '4th Year', 'Software Engineering'),
    ('2023-0005', 'Michael Wilson', '1st Year', 'Computer Science')
]

# Attendance status options
ATTENDANCE_STATUSES = ["Present", "Absent", "Excused"]
