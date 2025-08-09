import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience import logger
import os
from src.datascience.entity.config_entity import (DataTransformationConfig)
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data Splitted into training and testing sets")
        logger.info(f"train set shape {train.shape}")
        logger.info(f"test set shape {test.shape}")