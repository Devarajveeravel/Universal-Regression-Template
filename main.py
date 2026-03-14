from src.universal_regression.logging import logger
from src.universal_regression.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.universal_regression.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.universal_regression.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.universal_regression.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.universal_regression.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import sys
from src.universal_regression.exception import CustomException

# STAGE 1: DATA INGESTION
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)

# STAGE 2: DATA VALIDATION
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)

# STAGE 3: DATA TRANSFORMATION
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)

# STAGE 4: MODEL TRAINING
STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)

# STAGE 5: MODEL EVALUATION
STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)