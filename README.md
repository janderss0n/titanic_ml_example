# titanic_ml_example
ML example on Titanic dataset

## Run the API (app.py) in a docker container
Create image from Dockerfile:

docker build -t titanic_image .

Start a container with that image:

docker run -d --name titanic_api -p 12345:12345 titanic_image


Access the API via http://127.0.0.1:12345 and http://127.0.0.1:12345/predict as
long as the host='0.0.0.0' and port=12345 in the app.py file.
