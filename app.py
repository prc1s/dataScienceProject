from flask import Flask, render_template, request
import os, json
import yaml
import os 
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline


app = Flask(__name__)

@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    metrics_path = "artifacts/model_evaluation/metrics.json"
    params_path  = "params.yaml"

    try:
        with open(metrics_path) as f:
            metrics = json.load(f)
    except Exception as e:
        return str(e)
    try:
        with open(params_path) as f:
            params = yaml.safe_load(f) or {}
    except Exception as e:
        return str(e)

    return render_template(
        "train_results.html",
        metrics=metrics,
        params=params
    )


@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            form_data = [
            float(request.form['Age']),
            float(request.form['Sex']),
            float(request.form['RestingBP']),
            float(request.form['Cholesterol']),
            float(request.form['FastingBS']),
            float(request.form['MaxHR']),
            float(request.form['ExerciseAngina']),
            float(request.form['Oldpeak']),
            float(request.form['ChestPainType_ATA']),
            float(request.form['ChestPainType_NAP']),
            float(request.form['ChestPainType_TA']),
            float(request.form['RestingECG_Normal']),
            float(request.form['RestingECG_ST']),
            float(request.form['ST_Slope_Flat']),
            float(request.form['ST_Slope_Up'])
            ]

            X = np.array(form_data).reshape(1, -1)

            pipeline = PredictionPipeline()
            prediction = pipeline.predict(X)

            return render_template('result.html', prediction=prediction)

        except Exception as e:
            return render_template('result.html', error=str(e))

if __name__ == "__main__":
	
	app.run(host="0.0.0.0", port = 6767)