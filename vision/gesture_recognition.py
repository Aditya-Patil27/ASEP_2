import cv2
import numpy as np
import mediapipe as mp
from .camera_utils import Camera

class GestureRecognizer:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.camera = Camera()
        
    def detect_gesture(self):
        """
        Detect and classify hand gestures from camera feed
        Returns:
            str: Detected gesture ('FORWARD', 'BACKWARD', 'LEFT', 'RIGHT', 'STOP')
        """
        frame = self.camera.get_frame()
        if frame is None:
            return "STOP"
            
        # Convert to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        if not results.multi_hand_landmarks:
            return "STOP"
            
        # Get hand landmarks
        hand_landmarks = results.multi_hand_landmarks[0]
        
        # Draw landmarks for visualization
        self.mp_draw.draw_landmarks(
            frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            
        # Classify gesture based on landmark positions
        gesture = self._classify_gesture(hand_landmarks)
        
        return gesture
        
    def _classify_gesture(self, landmarks):
        """
        Classify gesture based on hand landmark positions
        Args:
            landmarks: MediaPipe hand landmarks
        Returns:
            str: Classified gesture
        """
        # Get key points
        thumb_tip = landmarks.landmark[4]
        index_tip = landmarks.landmark[8]
        middle_tip = landmarks.landmark[12]
        ring_tip = landmarks.landmark[16]
        pinky_tip = landmarks.landmark[20]
        wrist = landmarks.landmark[0]
        
        # Calculate angles and distances for gesture classification
        # This is a simplified example - you would want more sophisticated
        # gesture classification logic here
        
        # Example: Check if hand is open (all fingers extended)
        fingers_extended = all(
            finger.y < wrist.y for finger in [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip]
        )
        
        if fingers_extended:
            return "FORWARD"
        else:
            # Add more gesture classification logic here
            return "STOP"
            
    def __del__(self):
        self.camera.release() 