from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.components.data_validation import DataValidation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig
from src.datascience import logger

STAGE_NAME = "Data Ingestion Phase"

class DataIngestionTrainingPipeline:
   def __init__(self):
      pass
   
   def initiate_data_ingestion(slef):
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion()
    logger.info("Data Ingestion Configurations Retrieved!")
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.download_file()
    logger.info("Zip File Downloaded!")
    data_ingestion.extract_zip_file()
    logger.info("Unzipped th File!")
    logger.info("Data Ingestion Completed Sucessfully!")



if __name__ == '__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
    except Exception as e:
       logger.exception(e)
       raise e

