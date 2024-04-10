"""
This is a Python application that runs the machine learning
model for hand gesture recognition. When the web app sends a
picture of a hand gesture, this client processes the image,
passes it through the trained model, and determines the
corresponding emoji representation of the gesture.
"""

from flask import Flask
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import requests
import os

app = Flask(__name__)

# add functions for machine leanring client

def get_emoji_from_image(image_url):
    """
    Takes an image URL as input and returns an emoji representing the detected hand gesture.
    """
    label = generate_label(image_url)
    emoji_output = determine_emoji(label)
    return emoji_output


def generate_label(image_url):
    """
    Generates a label for the given image URL using the MediaPipe gesture recognizer model.
    """

    # Download the gesture recognizer model file
    url = "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task"
    response = requests.get(url)
    with open("gesture_recognizer.task", "wb") as file:
        file.write(response.content)

    # Create the GestureRecognizer object
    base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)

    # Load the image and recognize the gesture
    image = mp.Image.create_from_file(image_url)
    recognition_result = recognizer.recognize(image)

    # Get the top gesture and its category name
    top_gesture = recognition_result.gestures[0][0]
    category_name = top_gesture.category_name

    return category_name


def determine_emoji(self, hand_state):
    """
    Determines the appropriate emoji based on the given hand gesture label.
    """
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

# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
