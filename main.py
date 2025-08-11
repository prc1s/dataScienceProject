from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transfomation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
import os
STAGE_NAME = "Data Ingestion Phase"
try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Data Validation Phase"
try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Data Transoframtion Phase"
try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Model Training Phase"
try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Model Evaluation Phase"
try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
    
except Exception as e:
        logger.exception(e)
        raise e



