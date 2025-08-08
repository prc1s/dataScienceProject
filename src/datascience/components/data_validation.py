import requests
from urllib import request
from src.datascience import logger
import os
import zipfile
from src.datascience.entity.config_entity import (DataValidationConfig)
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            columns_validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            list_all_schema = self.config.all_schema["COLUMNS"].keys()

            logger.info("Validating Each Column in Data File")
            for column in all_columns:
                if column not in list_all_schema:
                    columns_validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {columns_validation_status}")

                else:
                    columns_validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {columns_validation_status}")
            logger.info(f"Validation Status {columns_validation_status} Recorded in {self.config.STATUS_FILE}")
            return columns_validation_status
        
        except Exception as e:
            logger.exception(e)
            raise e
