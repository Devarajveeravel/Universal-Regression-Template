from src.universal_regression.config.configuration import ConfigurationManager
from src.universal_regression.components.data_ingestion import DataIngestion
from src.universal_regression.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # 1. Initialize the Brain (reads YAML)
        config = ConfigurationManager()
        # 2. Get the specific instructions for Ingestion
        data_ingestion_config = config.get_data_ingestion_config()
        # 3. Give those instructions to the Worker
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # 4. Start the work
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(">>>>>> Stage Data Ingestion started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(">>>>>> Stage Data Ingestion completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e