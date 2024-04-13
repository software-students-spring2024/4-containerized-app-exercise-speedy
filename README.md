![lint-free](https://github.com/software-students-spring2024/4-containerized-app-exercise-speedy/actions/workflows/lint.yml/badge.svg)
![web_app CI/CD](https://github.com/software-students-spring2024/4-containerized-app-exercise-speedy/actions/workflows/web_app.yml/badge.svg)
![machine_learning_client CI/CD](https://github.com/software-students-spring2024/4-containerized-app-exercise-speedy/actions/workflows/machine_learning_client.yml/badge.svg)
![web_app Docker Image](https://github.com/software-students-spring2024/4-containerized-app-exercise-speedy/actions/workflows/publish-docker-image.yml/badge.svg)

# To build + run:

From the root dir, run

`docker compose up --build`

# To build + run docker containers locally for ml_client + web_app + db:

In one terminal,

`docker network create project4`

`cd web_app`

`docker build -t web_app_image .`

`docker run -it --rm --name web_app_container -p 5000:5000 --network project4 web_app_image`

In another terminal,

`cd machine_learning_client`

`docker build -t ml_client_image .`

`docker run -it --rm --name ml_client_container -p 5001:5001 --network project4 ml_client_image`

In another another terminal,

`docker run --name mongodb -d -p 27017:27017 --network project4 mongo`

The three containers are now connected through a docker network.

The web-app image is also available on the Docker Hub at [iltenahmet/web-app:main](https://hub.docker.com/r/iltenahmet/web-app)

# Real-Time Hand Gesture Recognition Web App

This project is a web application that allows users to take pictures of hand gestures using their device's camera. The pictures are sent to a machine learning model running in a separate container, which analyzes the hand gestures and classifies them into corresponding emojis.

The application consists of three main components running in separate Docker containers:

- **Web App:** This is a Flask web application that provides the user interface. Users can access the web app through their browser, use their device's camera to take pictures of hand gestures, and see the corresponding emoji detected by the machine learning model.
- **Machine Learning Client:** This is a Python application that runs the machine learning model for hand gesture recognition. When the web app sends a picture of a hand gesture, this client processes the image, passes it through the trained model, and determines the corresponding emoji representation of the gesture.
- **Database:** A MongoDB database stores the pictures taken by users, the detected emojis, and any other relevant data. Both the web app and the machine learning client interact with this database.

# To run tests and check code coverage

`coverage run -m pytest`

`coverage report -m`

### Contributors

* [Shriya Kalakata](https://github.com/shriyakalakata)
* [Ahmet Ilten](https://github.com/iltenahmet)
* [Glenda Boeker](https://github.com/gboeker)
* [Amber Li](https://github.com/al6862)
