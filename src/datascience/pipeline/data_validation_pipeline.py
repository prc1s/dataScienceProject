
from src.datascience.components.data_validation import DataValidation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience import logger

STAGE_NAME = "Data Validation Phase"

class DataValidationTrainingPipeline:
   def __init__(self):
      pass
   
   def initiate_data_ingestion(slef):
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation()
    logger.info("Data validation Configurations Retrieved!")
    data_validation = DataValidation(data_validation_config)
    data_validation.validate_all_columns()
    logger.info("Data Validation Completed Sucessfully!")



if __name__ == '__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
    except Exception as e:
       logger.exception(e)
       raise e

