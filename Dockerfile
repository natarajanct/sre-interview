# Use official python runtime as a parent image
FROM python:3.9.6-alpine3.13 as dev
FROM dev as runtime

# set work directory to /app
WORKDIR /app

# Copy current directory contents into the container under /app
COPY ./requirements.txt /app/
COPY ./src/app.py /app/app.py
COPY ./src/templates/index.html /app/templates/index.html

# Install required packages
RUN pip install -r /app/requirements.txt

# Env
ENV FLASK_APP=app.py

# run Flask
CMD flask run -h 0.0.0 -p 9001