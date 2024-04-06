"""
This is a Flask web application that provides the user interface. 
Users can access the web app through their browser, use their
device's camera to take pictures of hand gestures, and see the
corresponding emoji detected by the machine learning model.
"""

import os
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    default page
    """
    return "default page"


@app.route("/display")
def display():
    """
    This will render the display.html template which shows the results after the ML client.
    """


@app.route("/upload_image", methods=["POST"])
def upload_image():
    """
    Send the initial unprocessed image to MongoDB.
    """
    return "photo saved"


# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
