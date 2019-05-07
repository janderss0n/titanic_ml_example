import pickle
import pandas as pd
from flask import Flask, request

from preprocess_data import preprocess_data


app = Flask (__name__)


@app.route('/')
def hello():
    return 'Welcome to ML model API. Use /predict to make a prediction. \
    Use /input_ex to get an example of how the input should look like.'


@app.route('/input_ex')
def input_ex():
    return """[
    {"PassengerId": 1,"Pclass": 1,"Name": "Jessica Andersson","Sex": "female","Age": 26, "Cabin": "C07", "Embarked": "S"},
	{"PassengerId": 1,"Pclass": 3,"Name": "Jessica Andersson","Sex": "female","Age": 26, "Cabin": "C07", "Embarked": "C"}
    ]"""


@app.route('/predict', methods=['POST'])
def predict():
    model_filename = 'model_titanic_survival.pkl'
    interesting_columns = ['Pclass', 'Sex', 'Age', 'Cabin', 'Embarked']
    median_age = 28

    json_ = request.json
    df = pd.DataFrame(json_)

    processed_df = preprocess_data(df, interesting_columns, median_age)
    features = processed_df.select_dtypes(include='number')

    loaded_model = pickle.load(open(model_filename, 'rb'))
    prediction = loaded_model.predict(features)
    df['prediction'] = prediction
    return str(df.to_json(orient='records', force_ascii=False))


if __name__=='__main__':
    app.run(debug=True, port=12345)
