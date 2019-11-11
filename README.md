# Simple Web Application Prototype

This project was used to demonstrate how to connect a front end web page to
a back end REST API server.

You can easily run this within your local environment either by using the
Python interpreter directly or you can start it using docker.

## Run via Python Virtual Environment

Create a new virtual environment and install the required packages.

```bash
$ virtualenv --python=/usr/bin/python3.6 venv
$ source venv/bin/activate
(venv) pip install -r reqirements.txt
```

Once you have your virtual environment created/setup. Go ahead and run the
following command to start the web server.

```bash
$ gunicorn -w 1 -b 0.0.0.0:8081 wsgi:app
```

That is it, you now have the web server running locally in your environment.
You can access it by the following: http://0.0.0.0:8081

## Run via Docker

First you will need to build the image.

```bash
$ docker build -t webserver-poc:latest .
```

Once the image is built, you will need to start it.

```bash
$ docker run -it -p 0.0.0.0:8081:8081 <image>
```

That is it, you now have the web server running locally in your environment.
You can access it by the following: http://0.0.0.0:8081

## Available API resources

http://0.0.0.0:8081/app/api/v1/requests/create

## Availabe views

http://0.0.0.0:8081/
http://0.0.0.0:8081/requests/create
