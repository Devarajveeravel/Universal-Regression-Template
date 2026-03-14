import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
import os

# [NO-TOUCH ZONE]: Prediction Logic
# WHY: This class loads the "Brain" (model.joblib) we created in Stage 04
# and uses it to give an answer to the web app.
class PredictionPipeline:
    def __init__(self):
        # We point to the specific path where the model was saved
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    # [CUSTOMIZE ZONE]: The Predict Function
    # WHY: This takes the list of 11 numbers from your website and 
    # tells the model to calculate the quality.
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction