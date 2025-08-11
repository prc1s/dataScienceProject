import os
import pandas as pd
import mlflow
from pathlib import Path
from src.datascience.utils.common import save_json
import mlflow.sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evaluate_metrics(self, actual, predicted):
        rsme = np.sqrt(mean_squared_error(actual,predicted))
        mae = mean_absolute_error(actual,predicted)
        r2 = r2_score(actual, predicted)
        return rsme, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_experiment(self.config.experiment_name)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (rsme, mae, r2) = self.evaluate_metrics(test_y, predicted_qualities)

            scores = {"rsme":rsme, "mae":mae, "r2":r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rsme", rsme)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            mlflow.log_artifact(self.config.model_path, artifact_path="model")


