# pull official base image
FROM python:3.8.3-slim-buster

# # install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app
