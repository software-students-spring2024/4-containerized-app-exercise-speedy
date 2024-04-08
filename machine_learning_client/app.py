"""
This is a Python application that runs the machine learning
model for hand gesture recognition. When the web app sends a
picture of a hand gesture, this client processes the image,
passes it through the trained model, and determines the
corresponding emoji representation of the gesture.
"""

from flask import Flask
import cv2
import mediapipe

app = Flask(__name__)

# add functions for machine leanring client

test_image = cv2.imread("path_to_image.jpg")

# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
