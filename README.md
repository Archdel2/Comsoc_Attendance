# COMSOC Attendance Management System

A comprehensive attendance management system built with PyQt5 that includes QR code scanning capabilities for tracking student attendance at events. **Now updated to use MySQL database!**

## Features

- **Student Management**: Maintain a masterlist of students with ID, name, year level, and course
- **Event Management**: Create and manage events with automatic attendance tracking
- **QR Code Scanning**: Scan QR codes to automatically mark students as present
- **Attendance Tracking**: View and modify attendance status (Present, Absent, Excused)
- **Database Storage**: MySQL database for robust, scalable data storage
- **Modern UI**: Clean, intuitive interface built with PyQt5

## Project Structure

The code has been organized into logical, maintainable modules:

```
Attendance/
├── run.py               # Main application launcher
├── main_app.py          # Main application logic
├── database.py          # MySQL database operations
├── ui_pages.py          # UI page components
├── camera_scanner.py    # Camera and QR code scanning
├── config.py            # Configuration and environment variables
├── requirements.txt     # Python dependencies
├── .env                 # Environment configuration (MySQL credentials)
├── test_db_connection.py # Database connection tester
├── README.md            # This file
└── README_MYSQL.md     # Detailed MySQL setup instructions
```

## Prerequisites

- **MySQL Server** running with database `comsoc_attendance` created
- **Python 3.7+** with pip
- **Camera** for QR code scanning functionality

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Database**:
   - Edit `.env` file with your MySQL credentials
   - Ensure database `comsoc_attendance` exists

3. **Test Database Connection**:
   ```bash
   python test_db_connection.py
   ```

4. **Run the Application**:
   ```bash
   python run.py
   ```

## Database Schema

The system uses four main tables matching your MySQL structure:

- **Students**: Student information (student_id, fname, year_level, course)
- **Events**: Event details (event_id, event_name, event_date)
- **AttendanceRecords**: Attendance record metadata (record_id, record_name, event_id)
- **Attendance**: Actual attendance data (student details, status, timestamp)

## Configuration

Edit `.env` file to configure:
- MySQL database connection settings
- Application dimensions and camera settings
- UI styling preferences

## Dependencies

- **PyQt5**: GUI framework
- **OpenCV**: Camera operations
- **pyzbar**: QR code decoding
- **NumPy**: Numerical operations
- **mysql-connector-python**: MySQL database connectivity
- **python-dotenv**: Environment variable management

## Usage

### Main Menu
- **View Events**: Access event management
- **View Masterlist**: View student database

### Event Management
- Create new events
- View existing events
- Double-click an event to view attendance

### Attendance Tracking
- View attendance for specific events
- Manually modify attendance status
- Use QR code scanner for automatic attendance

### QR Code Scanner
- Point camera at student QR codes
- Automatically marks students as present
- Real-time feedback and status updates

## Migration from SQLite

If you're upgrading from the SQLite version:
1. Export existing data
2. Create MySQL database structure
3. Import data into new tables
4. Update configuration files
5. Test connection and run

## Troubleshooting

### Database Issues
- Run `test_db_connection.py` to verify MySQL connection
- Check MySQL server is running
- Verify database permissions and credentials
- Ensure database `comsoc_attendance` exists

### Camera Issues
- Ensure camera is not in use by other applications
- Check camera permissions
- Verify OpenCV installation

### Import Errors
- Verify all dependencies are installed
- Check Python path and module locations

## Support

For detailed MySQL setup and troubleshooting, see `README_MYSQL.md`.

## License

This project is for educational and organizational use.

## Contributing

1. Follow the existing code structure
2. Add proper documentation
3. Test changes thoroughly
4. Update requirements.txt if adding new dependencies
