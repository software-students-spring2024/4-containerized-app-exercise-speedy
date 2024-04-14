"""
This is a Python application that runs the machine learning
model for hand gesture recognition. When the web app sends a
picture of a hand gesture, this client processes the image,
passes it through the trained model, and determines the
corresponding emoji representation of the gesture.
"""

from bson import ObjectId
from flask import Flask, request
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import requests
import os
from pymongo import MongoClient


app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongodb:27017/"))
db = client.test


def get_emoji_from_image(image_url):
    """
    Takes an image URL as input and returns an emoji representing the detected hand gesture.
    """
    label = generate_label(image_url)
    # emoji_output = determine_emoji(label)
    # return emoji_output
    return label


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
    base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)

    # Load the image and recognize the gesture
    image = mp.Image.create_from_file(image_url)
    recognition_result = recognizer.recognize(image)

    # Get the top gesture and its category name
    top_gesture = recognition_result.gestures[0][0]
    category_name = top_gesture.category_name

    return category_name


'''
def determine_emoji(self, hand_label):
    """
    Determines the appropriate emoji based on the given hand gesture label.
    """
    if hand_label == 0:
        return "No emoji detected"
    if hand_label == 1:
        return "Thumbs up! 👍"
    elif hand_label == 2:
        return "Thumbs down! 👎"
    elif hand_label == 3:
        return "Peace! ✌️"
    elif hand_label == 4:
        return "Finger up! ☝️"
    elif hand_label == 5:
        return "Right on! ✊"  # maybe change the wording here
    elif hand_label == 6:
        return "Hello! 👋"
    elif hand_label == 7:
        return "I love you! 👍"
    return "None"
'''


@app.route("/processImage", methods=["POST"])
def process_image():
    image_id = request.json.get("image_id")
    if image_id:
        # find the image data based on given id
        image_data = db.images.find_one({"_id": ObjectId(image_id)})["image_data"]
        # generate ml label MAKE THIS WORK
        # label_generated = generate_label(image_data) # TODO: UNCOMMENT THIS AND MAKE IT WORK, below is just temporary
        label_generated = "temp"
        # update db with the generated label
        db.images.update_one(
            {"_id": ObjectId(image_id)}, {"$set": {"mlResult": label_generated}}
        )
        return "Image processed successfully", 200
    else:
        return "Invalid request", 400


# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5001")
    app.run(port=FLASK_PORT, host="0.0.0.0")
