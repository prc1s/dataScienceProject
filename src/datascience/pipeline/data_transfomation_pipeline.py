from src.datascience.components.data_transformation import DataTransformation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataTransformationConfig

from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Phase"

class DataTransformationPipeline:
   def __init__(self):
      pass
   
   def initiate_data_transformation(slef):
        try:
            config = ConfigurationManager()
            config=config.get_data_validation()
            with open(Path(config.STATUS_FILE), 'r') as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation()
                logger.info("Data Transformation Configurations Retrieved!")
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_split()
                
            else:
                logger.info("Latest Data Validation Failed! Cannot Proceed")
        
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
    except Exception as e:
       logger.exception(e)
       raise e

