"""
This is a Python application that runs the machine learning
model for hand gesture recognition. When the web app sends a
picture of a hand gesture, this client processes the image,
passes it through the trained model, and determines the
corresponding emoji representation of the gesture.
"""

import os
import base64
from bson import ObjectId
from flask import Flask, request
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
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
    return label


def generate_label(image_url):
    """
    Generates a label for the given image URL using the MediaPipe gesture recognizer model.
    """
    # Create the GestureRecognizer object
    base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)

    # Write image to a temporary file for mediapipe to read from
    image_data = base64.b64decode(image_url.split(",")[1])
    temp_image_path = "temp_image.jpg"
    with open(temp_image_path, "wb") as f:
        f.write(image_data)

    # Load the image and recognize the gesture
    image = mp.Image.create_from_file(temp_image_path)
    recognition_result = recognizer.recognize(image)

    # Get the top gesture and its category name
    top_gesture = recognition_result.gestures[0][0]
    category_name = top_gesture.category_name

    # Remove temporary image file
    os.remove(temp_image_path)

    return category_name


@app.route("/processImage", methods=["POST"])
def process_image():
    """
    Process the image
    """
    image_id = request.json.get("image_id")
    if image_id:
        # find the image data based on given id
        image_data = db.images.find_one({"_id": ObjectId(image_id)})["image_data"]
        label_generated = generate_label(image_data)
        # update db with the generated label
        db.images.update_one(
            {"_id": ObjectId(image_id)}, {"$set": {"mlResult": label_generated}}
        )
        return "Image processed successfully", 200
    return "Invalid request", 400


# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5001")
    app.run(port=FLASK_PORT, host="0.0.0.0")
