import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configuration import ConfigurationManager

STAGE_NAME = "Training Phase"

class ModelTrainingPipeline:
   def __init__(self):
      pass
   
   def initiate_model_training(slef):
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer()
    logger.info("Model Trainer Configurations Retrieved!")
    model_trainer = ModelTrainer(model_trainer_config)
    model_trainer.train()




if __name__ == '__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} Initiated <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<\n\n x========x")
    except Exception as e:
       logger.exception(e)
       raise e

