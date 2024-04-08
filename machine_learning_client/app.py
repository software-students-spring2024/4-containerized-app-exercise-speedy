"""
This is a Python application that runs the machine learning
model for hand gesture recognition. When the web app sends a
picture of a hand gesture, this client processes the image,
passes it through the trained model, and determines the
corresponding emoji representation of the gesture.
"""

from flask import Flask
import cv2
import mediapipe as mp

app = Flask(__name__)

# add functions for machine leanring client

class HandGestureDetector:
    def __init__(self, static_image_mode = False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5):
        self.static_image_mode =static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands= self.mp_hands.Hands(self.static_image_mode,
                                        self.max_num_hands,
                                        self.min_detection_confidence,    
                                        self.min_tracking_confidence)
        
    def gesture_recognition(self, image):
        image = cv2.imread('images/test_image1.png')
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process image using MediaPipe hands module
        results = self.hands.process(image_rgb)
        
        # If hand(s) detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                pass
        
        # If no hand or gesture detected
        return 0
    
    def determine_emoji(self, hand_state):
        if hand_state == 0:
            return "No emoji detected"
        elif hand_state == 1:
            return "Thumbs up! 👍"
        elif hand_state == 2:
            return "Thumbs down! 👎"
        elif hand_state == 3:
            return "Thumbs up! 👍"
        elif hand_state == 4:
            return "Thumbs up! 👍"
        elif hand_state == 5:
            return "Right on! ✊" # maybe change the wording here
        elif hand_state == 6:
            return "Hello! 👋"
        elif hand_state == 7:
            return "I love you! 👍"

# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
