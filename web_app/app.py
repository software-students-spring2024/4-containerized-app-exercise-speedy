"""
This is a Flask web application that provides the user interface. 
Users can access the web app through their browser, use their
device's camera to take pictures of hand gestures, and see the
corresponding emoji detected by the machine learning model.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def display():
    return "display images here"


@app.route("/", methods=["GET", "POST"])
def image_capture():
    return "take picture here"


# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)
