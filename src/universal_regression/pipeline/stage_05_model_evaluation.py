from src.universal_regression.config.configuration import ConfigurationManager
from src.universal_regression.components.model_evaluation import ModelEvaluation
from src.universal_regression.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_custom = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_custom.save_results()