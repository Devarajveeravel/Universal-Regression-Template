import pandas as pd
import os
from src.universal_regression.logging import logger
from sklearn.linear_model import ElasticNet
import joblib # [TECH TERM]: Used to save the "Brain" as a file
from src.universal_regression.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # [NO-TOUCH ZONE]: Splitting Features and Target
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # [CUSTOMIZE ZONE]: The Math
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Save the model so we can use it in our App later
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model saved at {os.path.join(self.config.root_dir, self.config.model_name)}")