import cv2
import numpy as np

class Camera:
    def __init__(self, camera_id=0):
        """
        Initialize camera
        Args:
            camera_id (int): Camera device ID (default: 0 for primary camera)
        """
        self.camera = cv2.VideoCapture(camera_id)
        if not self.camera.isOpened():
            raise RuntimeError("Failed to open camera")
            
        # Set camera properties
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera.set(cv2.CAP_PROP_FPS, 30)
        
    def get_frame(self):
        """
        Capture and return a frame from the camera
        Returns:
            numpy.ndarray: Captured frame or None if capture failed
        """
        ret, frame = self.camera.read()
        if not ret:
            return None
            
        return frame
        
    def release(self):
        """Release the camera"""
        if self.camera is not None:
            self.camera.release()
            
    def __del__(self):
        self.release() 