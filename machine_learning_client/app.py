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
import os

app = Flask(__name__)

# add functions for machine leanring client


class HandGestureDetector:
    def __init__(
        self,
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5,
    ):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        print("init test")

        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            self.static_image_mode,
            self.max_num_hands,
            self.min_detection_confidence,
            self.min_tracking_confidence,
        )
        """

        # Initialize MediaPipe gesture module
        self.mp_gesture = mp.solutions.gesture
        self.gesture = self.mp_gesture.Gesture(
            static_image_mode=False,
            max_num_hands=1,
            gesture_model_context=self.mp_gesture.GestureModelContext(
                min_tracking_confidence=0.5
            ),
        )

    def gesture_recognition(self, image):
        image = cv2.imread(image)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        """
        # Process image using MediaPipe hands module
        results = self.hands.process(image_rgb)

        # If hand(s) detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                pass

        # If no hand or gesture detected
        return 0
        """

        # Process image using MediaPipe gesture module
        gesture_results = self.gesture.process(image_rgb)

        # If gesture(s) detected
        if gesture_results.multi_handedness:
            # Iterate through detected gestures
            for _, gesture in zip(
                gesture_results.multi_handedness, gesture_results.multi_gestures
            ):
                num = 0
                # Classify gesture
                if gesture.label == "Thumb_Up":
                    print("Thumbs up!")
                elif gesture.label == "Thumb_Down":
                    print("Thumbs down!")

        print("gesture recog test")

    def determine_emoji(self, hand_state):
        print("emoji test")
        if hand_state == 0:
            return "No emoji detected"
        elif hand_state == 1:
            return "Thumbs up! 👍"
        elif hand_state == 2:
            return "Thumbs down! 👎"
        elif hand_state == 3:
            return "Peace! ✌️"
        elif hand_state == 4:
            return "Finger up! ☝️"
        elif hand_state == 5:
            return "Right on! ✊"  # maybe change the wording here
        elif hand_state == 6:
            return "Hello! 👋"
        elif hand_state == 7:
            return "I love you! 👍"
        return "None"


def main():
    print("main test")
    detector = HandGestureDetector()
    output = detector.gesture_recognition("images/test_image1.png")
    print(output, "+", output)


# run the app
if __name__ == "__main__":
    main()
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
