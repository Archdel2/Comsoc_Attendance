"""
Camera and QR code scanning functionality for the Attendance Management System
"""

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from config import CAMERA_UPDATE_INTERVAL, CAMERA_DISPLAY_WIDTH, CAMERA_DISPLAY_HEIGHT


class CameraScanner:
    """Handles camera operations and QR code scanning"""
    
    def __init__(self, camera_label, status_label, parent):
        self.camera_label = camera_label
        self.status_label = status_label
        self.parent = parent
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
    
    def start_camera(self):
        """Start the camera and begin scanning"""
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            self.timer.start(CAMERA_UPDATE_INTERVAL)
        else:
            self.status_label.setText("Error: Could not open camera")
    
    def stop_camera(self):
        """Stop the camera and timer"""
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None
    
    def update_frame(self):
        """Update camera frame and scan for QR codes"""
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Convert frame to RGB for QR detection
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Decode QR codes
                decoded_objects = decode(rgb_frame)
                
                for obj in decoded_objects:
                    # Draw rectangle around QR code
                    points = obj.polygon
                    if len(points) > 4:
                        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                        hull = list(map(tuple, np.squeeze(hull)))
                    else:
                        hull = points
                    
                    n = len(hull)
                    for j in range(0, n):
                        cv2.line(frame, hull[j], hull[(j+1) % n], (0, 255, 0), 3)
                    
                    # Process QR code data
                    data = obj.data.decode('utf-8')
                    self.process_qr_code(data)
                
                # Convert frame to QImage and display
                self.display_frame(frame)
    
    def display_frame(self, frame):
        """Convert OpenCV frame to QImage and display it"""
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qt_image).scaled(
            CAMERA_DISPLAY_WIDTH, CAMERA_DISPLAY_HEIGHT, 
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.camera_label.setPixmap(pixmap)
    
    def process_qr_code(self, data):
        """Process scanned QR code data"""
        try:
            student_id = data.strip()
            
            self.parent.db.mark_student_present(self.parent.current_event_id, student_id)
            
            self.parent.populate_attendance_table(self.parent.current_event_id)
            
            self.status_label.setText(f"Scanned: {student_id} marked as Present")
            
            QTimer.singleShot(2000, lambda: self.status_label.setText("Point camera at QR code"))
            
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")
    
    def is_camera_active(self):
        """Check if camera is currently active"""
        return self.cap is not None and self.cap.isOpened()
