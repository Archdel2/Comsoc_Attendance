#!/usr/bin/env python3
"""
Test script to verify MySQL database connection
"""

import sys
import os

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from database import DatabaseManager
    from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    
    print("Testing MySQL database connection...")
    print(f"Host: {DB_HOST}")
    print(f"Port: {DB_PORT}")
    print(f"Database: {DB_NAME}")
    print(f"User: {DB_USER}")
    print(f"Password: {'*' * len(DB_PASSWORD) if DB_PASSWORD else '(empty)'}")
    print()
    
    # Test connection
    db = DatabaseManager()
    print("✓ Database connection successful!")
    
    # Test table creation
    db.create_tables()
    print("✓ Tables created/verified successfully!")
    
    # Test sample data import
    db.import_sample_data()
    print("✓ Sample data imported successfully!")
    
    # Test data retrieval
    students = db.get_all_students()
    print(f"✓ Retrieved {len(students)} students from database")
    
    events = db.get_all_events()
    print(f"✓ Retrieved {len(events)} events from database")
    
    # Close connection
    db.close()
    print("✓ Database connection closed successfully!")
    
    print("\n🎉 All tests passed! Your MySQL database is working correctly.")
    
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please install required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure MySQL server is running")
    print("2. Verify database 'comsoc_attendance' exists")
    print("3. Check your .env file configuration")
    print("4. Ensure MySQL user has proper permissions")
    sys.exit(1)
