# titanic_ml_example
ML example on Titanic dataset

## Run the API (app.py) in a docker container
Create image from Dockerfile:

docker build -t titanic_image .

Start a container with that image:

docker run -d --name titanic_api -p 12345:12345 titanic_image



