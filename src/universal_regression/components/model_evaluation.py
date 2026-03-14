import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.universal_regression.utils.common import save_json
from src.universal_regression.entity import ModelEvaluationConfig
import numpy as np
import joblib
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    # [NO-TOUCH ZONE]: Math functions for evaluation
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted_qualities = model.predict(test_x)

        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
        
        # [TECH TERM]: Saving metrics to JSON
        # WHY: This allows other apps (like a web dashboard) to read your model's accuracy.
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        save_json(path=Path(self.config.metric_file_name), data=scores)