from src.universal_regression.config.configuration import ConfigurationManager
from src.universal_regression.components.model_trainer import ModelTrainer
from src.universal_regression.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_comp = ModelTrainer(config=model_trainer_config)
        model_trainer_comp.train()