![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# To build + run docker image locally for web_app:
docker build -t web_app_image .

docker run -it --rm --name web_app_container web_app_image

from here: https://hub.docker.com/_/python

# To build + run docker image locally for db:

docker run --name mongodb -d -p 27017:27017 mongo

# Real-Time Hand Gesture Recognition Web App

This project is a web application that allows users to take pictures of hand gestures using their device's camera. The pictures are sent to a machine learning model running in a separate container, which analyzes the hand gestures and classifies them into corresponding emojis.

The application consists of three main components running in separate Docker containers:

* Web App: This is a Flask web application that provides the user interface. Users can access the web app through their browser, use their device's camera to take pictures of hand gestures, and see the corresponding emoji detected by the machine learning model.
* Machine Learning Client: This is a Python application that runs the machine learning model for hand gesture recognition. When the web app sends a picture of a hand gesture, this client processes the image, passes it through the trained model, and determines the corresponding emoji representation of the gesture.
* Database: A MongoDB database stores the pictures taken by users, the detected emojis, and any other relevant data. Both the web app and the machine learning client interact with this database.

### Contributors

* [Shriya Kalakata](https://github.com/shriyakalakata)
* [Ahmet Ilten](https://github.com/iltenahmet)
* [Glenda Boeker](https://github.com/gboeker)
* [Amber Li](https://github.com/al6862)