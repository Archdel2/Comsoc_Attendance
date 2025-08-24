#!/usr/bin/env python3
"""
Test script to verify GUI components can be imported and initialized
"""

import sys
import os

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    print("Testing GUI component imports...")
    
    # Test importing main components
    from config import APP_TITLE, APP_WIDTH, APP_HEIGHT
    print(f"Config imported: {APP_TITLE} ({APP_WIDTH}x{APP_HEIGHT})")
    
    from database import DatabaseManager
    print("Database module imported")
    
    from ui_pages import MainPage, EventsPage, MasterlistPage, AttendancePage, ScannerPage
    print("UI pages imported")
    
    from camera_scanner import CameraScanner
    print("Camera scanner imported")
    
    from main_app import MainWindow
    print("Main application imported")
    
    print("\nAll GUI components imported successfully!")
    print("The application should work properly now.")
    
except ImportError as e:
    print(f"Import Error: {e}")
    print("Please install required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
