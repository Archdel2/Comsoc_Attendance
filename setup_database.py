#!/usr/bin/env python3
"""
Database setup script for COMSOC Attendance System
Creates the MySQL database tables if they don't exist
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from database import DatabaseManager
    from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    
    print("Setting up COMSOC Attendance database...")
    print(f"Database: {DB_NAME}")
    print(f"Host: {DB_HOST}:{DB_PORT}")
    print(f"User: {DB_USER}")
    print()
    
    db = DatabaseManager()
    
    print("Creating database tables...")
    db.create_tables()
    
    print("Importing sample student data...")
    db.import_sample_data()
    
    students = db.get_all_students()
    print(f"Database setup complete!")
    print(f"{len(students)} students imported")
    print(f"Tables created successfully")
    
    db.close()
    
    print("\n🎉 Database setup completed successfully!")
    print("You can now run the application with: python run.py")
    
except ImportError as e:
    print(f"Import Error: {e}")
    print("Please install required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Setup Error: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure MySQL server is running")
    print("2. Verify database 'comsoc_attendance' exists")
    print("3. Check your .env file configuration")
    print("4. Ensure MySQL user has proper permissions")
    print("5. Try running: python test_db_connection.py")
    sys.exit(1)
