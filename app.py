from flask import Flask, render_template, request
import os
import numpy as np
from src.universal_regression.pipeline.prediction import PredictionPipeline

# [CUSTOMIZE ZONE]: template_folder='.'
# WHY: This allows Flask to find index.html in your main folder without a 'templates' sub-folder.
app = Flask(__name__, template_folder='.') 

@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!"

@app.route('/predict', methods=['POST'])
def index():
    if request.method == 'POST':
        try:
            data = [
                float(request.form['fixed_acidity']),
                float(request.form['volatile_acidity']),
                float(request.form['citric_acid']),
                float(request.form['residual_sugar']),
                float(request.form['chlorides']),
                float(request.form['free_sulfur_dioxide']),
                float(request.form['total_sulfur_dioxide']),
                float(request.form['density']),
                float(request.form['pH']),
                float(request.form['sulphates']),
                float(request.form['alcohol'])
            ]
            
            data_array = np.array(data).reshape(1, -1)
            
            obj = PredictionPipeline()
            predict = obj.predict(data_array)

            # Returning the result in a clean way
            return f"""
            <div style="background:#0f172a; color:white; height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; font-family:sans-serif;">
                <h1 style="color:#00d2ff;">Predicted Quality: {round(predict[0], 2)}</h1>
                <a href="/" style="color:white; text-decoration:none; border:1px solid white; padding:10px 20px; border-radius:5px;">Predict Another</a>
            </div>
            """

        except Exception as e:
            return f'Something went wrong: {e}'

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)