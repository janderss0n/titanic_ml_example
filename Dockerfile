FROM python:3.7

RUN mkdir /app

COPY preprocess_data.py /app
COPY requirements.txt /app
COPY model_titanic_survival.pkl /app
COPY app.py /app

WORKDIR /app

RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
