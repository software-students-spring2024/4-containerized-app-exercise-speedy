"""
This is a Flask web application that provides the user interface. 
Users can access the web app through their browser, use their
device's camera to take pictures of hand gestures, and see the
corresponding emoji detected by the machine learning model.
"""

import os
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
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
    Send the initial unprocessed image to MongoDB.
    """
    image_data = request.form["image_data"]
    db.images.insert_one({"image_data": image_data})
    return redirect(url_for("display"))


# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
