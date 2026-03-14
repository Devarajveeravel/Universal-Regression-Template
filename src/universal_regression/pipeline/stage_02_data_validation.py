from src.universal_regression.config.configuration import ConfigurationManager
from src.universal_regression.components.data_validation import DataValidation
from src.universal_regression.logging import logger
import sys

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # 1. Start the Brain
        config = ConfigurationManager()
        # 2. Get Validation Rules
        data_validation_config = config.get_data_validation_config()
        # 3. Initialize the Security Guard
        data_validation = DataValidation(config=data_validation_config)
        # 4. Run the Check
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(">>>>>> Stage Data Validation started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(">>>>>> Stage Data Validation completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e