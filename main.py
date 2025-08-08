from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
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
        obj.initiate_data_ingestion()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
except Exception as e:
       logger.exception(e)
       raise e