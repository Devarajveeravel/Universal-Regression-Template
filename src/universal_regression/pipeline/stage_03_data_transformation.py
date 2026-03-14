from src.universal_regression.config.configuration import ConfigurationManager
from src.universal_regression.components.data_transformation import DataTransformation
from src.universal_regression.logging import logger
from pathlib import Path

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # [NO-TOUCH ZONE]: Standard Pipeline Logic
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()