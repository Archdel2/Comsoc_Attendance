"""
UI page components for the Attendance Management System
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLabel, QTableWidget, QTableWidgetItem, QComboBox, 
                             QLineEdit, QHeaderView, QAbstractItemView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from config import BUTTON_STYLE, ATTENDANCE_STATUSES


class MainPage(QWidget):
    """Main page with navigation buttons"""
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the main page UI"""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("COMSOC Attendance Recorder")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("padding: 30px; color: #2c3e50;")
        
        # Buttons
        view_events_btn = QPushButton("View Events")
        view_events_btn.setStyleSheet(BUTTON_STYLE)
        view_events_btn.clicked.connect(self.parent.show_events_page)
        
        view_masterlist_btn = QPushButton("View Masterlist")
        view_masterlist_btn.setStyleSheet(BUTTON_STYLE)
        view_masterlist_btn.clicked.connect(self.parent.show_masterlist_page)
        
        # Layout
        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(view_events_btn)
        layout.addWidget(view_masterlist_btn)
        layout.addStretch()
        
        self.setLayout(layout)


class EventsPage(QWidget):
    """Events management page"""
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the events page UI"""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Events")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        
        # Back button
        back_btn = QPushButton("Back to Main")
        back_btn.clicked.connect(lambda: self.parent.central_widget.setCurrentWidget(self.parent.main_page))
        
        # Add event section
        add_event_layout = QHBoxLayout()
        self.event_name_input = QLineEdit()
        self.event_name_input.setPlaceholderText("Enter event name")
        add_event_btn = QPushButton("Add New Event")
        add_event_btn.clicked.connect(self.parent.add_event)
        
        add_event_layout.addWidget(self.event_name_input)
        add_event_layout.addWidget(add_event_btn)
        
        # Events table
        self.events_table = QTableWidget()
        self.events_table.setColumnCount(2)
        self.events_table.setHorizontalHeaderLabels(["Event Name", "Date Created"])
        self.events_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.events_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.events_table.cellDoubleClicked.connect(self.parent.view_event_records)
        
        # Layout
        layout.addWidget(back_btn)
        layout.addWidget(title)
        layout.addLayout(add_event_layout)
        layout.addWidget(self.events_table)
        
        self.setLayout(layout)


class RecordsPage(QWidget):
    """Records management page for a specific event"""
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the records page UI"""
        layout = QVBoxLayout()
        
        # Title
        self.records_title = QLabel()
        self.records_title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.records_title.setFont(title_font)
        
        # Back button
        back_btn = QPushButton("Back to Events")
        back_btn.clicked.connect(lambda: self.parent.central_widget.setCurrentWidget(self.parent.events_page))
        
        # Add record section
        add_record_layout = QHBoxLayout()
        self.record_name_input = QLineEdit()
        self.record_name_input.setPlaceholderText("Enter record name (e.g., Morning Sign-in)")
        add_record_btn = QPushButton("Add New Record")
        add_record_btn.clicked.connect(self.parent.add_attendance_record)
        
        add_record_layout.addWidget(self.record_name_input)
        add_record_layout.addWidget(add_record_btn)
        
        # Records table
        self.records_table = QTableWidget()
        self.records_table.setColumnCount(2)
        self.records_table.setHorizontalHeaderLabels(["Record Name", "Date Created"])
        self.records_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.records_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.records_table.cellDoubleClicked.connect(self.parent.view_record_students)
        
        # Layout
        layout.addWidget(back_btn)
        layout.addWidget(self.records_title)
        layout.addLayout(add_record_layout)
        layout.addWidget(self.records_table)
        
        self.setLayout(layout)


class MasterlistPage(QWidget):
    """Student masterlist page"""
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the masterlist page UI"""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Student Masterlist")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        
        # Back button
        back_btn = QPushButton("Back to Main")
        back_btn.clicked.connect(lambda: self.parent.central_widget.setCurrentWidget(self.parent.main_page))
        
        # Search section
        search_layout = QHBoxLayout()
        self.masterlist_search_input = QLineEdit()
        self.masterlist_search_input.setPlaceholderText("Search by ID, Name, Year Level, or Course...")
        self.masterlist_search_input.textChanged.connect(self.parent.filter_masterlist_table)
        
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.masterlist_search_input)
        search_layout.addStretch()
        
        # --- QR Code Button ---
        qr_btn_layout = QHBoxLayout()
        generate_qr_btn = QPushButton("Generate QR Codes for All Students")
        generate_qr_btn.setStyleSheet(BUTTON_STYLE)
        generate_qr_btn.clicked.connect(self.parent.generate_qr_codes_for_all_students)
        qr_btn_layout.addStretch()
        qr_btn_layout.addWidget(generate_qr_btn)
        qr_btn_layout.addStretch()
        
        # Masterlist table
        self.masterlist_table = QTableWidget()
        self.masterlist_table.setColumnCount(4)
        self.masterlist_table.setHorizontalHeaderLabels(["Student ID", "First Name", "Year Level", "Course"])
        self.masterlist_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.masterlist_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Layout
        layout.addWidget(back_btn)
        layout.addWidget(title)
        layout.addLayout(search_layout)
        layout.addLayout(qr_btn_layout)
        layout.addWidget(self.masterlist_table)
        
        
        self.setLayout(layout)


class AttendancePage(QWidget):
    """Attendance management page"""
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the attendance page UI"""
        layout = QVBoxLayout()
        
        self.attendance_title = QLabel()
        self.attendance_title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.attendance_title.setFont(title_font)
        
        # Back button
        back_btn = QPushButton("Back to Records")
        back_btn.clicked.connect(lambda: self.parent.central_widget.setCurrentWidget(self.parent.records_page))
        
        # Check attendance button
        check_attendance_btn = QPushButton("Check Attendance (Scan QR)")
        check_attendance_btn.clicked.connect(self.parent.show_scanner_page)
        
        # Export button
        export_btn = QPushButton("Export to Excel")
        export_btn.clicked.connect(self.parent.export_attendance_to_excel)
        
        # Search and filter section
        search_filter_layout = QHBoxLayout()
        
        # Search bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by ID, Name, Year Level, or Course...")
        self.search_input.textChanged.connect(self.parent.filter_attendance_table)
        
        # Status filter dropdown
        self.status_filter = QComboBox()
        self.status_filter.addItem("All Statuses")
        self.status_filter.addItems(ATTENDANCE_STATUSES)
        self.status_filter.currentTextChanged.connect(self.parent.filter_attendance_table)
        
        search_filter_layout.addWidget(QLabel("Search:"))
        search_filter_layout.addWidget(self.search_input)
        search_filter_layout.addWidget(QLabel("Status:"))
        search_filter_layout.addWidget(self.status_filter)
        search_filter_layout.addStretch()
        
        # Attendance table
        self.attendance_table = QTableWidget()
        self.attendance_table.setColumnCount(6)
        self.attendance_table.setHorizontalHeaderLabels(["Student ID", "First Name", "Year Level", "Course", "Timestamp", "Status"])
        self.attendance_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Layout
        layout.addWidget(back_btn)
        layout.addWidget(self.attendance_title)
        layout.addWidget(check_attendance_btn)
        layout.addWidget(export_btn)
        layout.addLayout(search_filter_layout)
        layout.addWidget(self.attendance_table)
        
        self.setLayout(layout)


class ScannerPage(QWidget):
    """QR code scanner page"""
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the scanner page UI"""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("QR Code Scanner")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        
        # Camera display
        self.camera_label = QLabel()
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setMinimumSize(640, 480)
        self.camera_label.setStyleSheet("border: 1px solid black; background-color: #eee;")
        
        # Status message
        self.scanner_status = QLabel("Point camera at QR code")
        self.scanner_status.setAlignment(Qt.AlignCenter)
        
        # Back button
        back_btn = QPushButton("Back to Attendance")
        back_btn.clicked.connect(self.parent.stop_camera_and_go_back)
        
        # Layout
        layout.addWidget(title)
        layout.addWidget(self.camera_label)
        layout.addWidget(self.scanner_status)
        layout.addWidget(back_btn)
        
        self.setLayout(layout)
