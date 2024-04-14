"""
This is a Flask web application that provides the user interface. 
Users can access the web app through their browser, use their
device's camera to take pictures of hand gestures, and see the
corresponding emoji detected by the machine learning model.
"""

import os
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient

import requests

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongodb:27017/"))
db = client.test


@app.route("/", methods=["GET", "POST"])
def index():
    """
    default page
    """
    return render_template("upload_image.html")


@app.route("/display")
def display():
    """
    This will render the display.html template which shows the results after the ML client.
    """
    images = db.images.find()
    return render_template("display.html", images=images)


@app.route("/upload_image", methods=["POST"])
def upload_image():
    """
    Send the initial unprocessed image to MongoDB,
    then trigger ml client, and redirect to display.
    """
    image_data = request.form["image_data"]
    image_id = db.images.insert_one({"image_data": image_data}).inserted_id
    # Make a request to the ML client to process the image
    ml_client_url = "http://machine_learning_client:5001/processImage"
    response = requests.post(ml_client_url, json={"image_id": str(image_id)})
    if response.status_code == 200:
        return redirect(url_for("display"))
    return "Error processing image"


# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5002")
    app.run(port=FLASK_PORT, host="0.0.0.0")
