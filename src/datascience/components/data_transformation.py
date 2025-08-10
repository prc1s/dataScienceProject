import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience import logger
import os
from src.datascience.entity.config_entity import (DataTransformationConfig)
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def preprocess_data(self):
        df = pd.read_csv(self.config.data_path)

        target = self.config.target_column
        if target not in df.columns:
            raise ValueError(f"Target column '{target}' not found.")

        if "Sex" in df.columns:
            sex_norm = (
                df["Sex"].astype(str).str.strip().str.upper()
                .replace({"MALE": "M", "FEMALE": "F"})
            )
            df["Sex"] = sex_norm.map({"M": 1, "F": 0}).astype("float64")

        if "ExerciseAngina" in df.columns:
            ang_norm = df["ExerciseAngina"].astype(str).str.strip().str.upper()
            df["ExerciseAngina"] = ang_norm.map({"Y": 1, "N": 0}).astype("float64")

        cat_cols = []
        for c in ["ChestPainType", "RestingECG", "ST_Slope"]:
            if c in df.columns:
                cat_cols.append(c)

        if cat_cols:
            df = pd.get_dummies(df, columns=cat_cols, drop_first=True, dtype="float64")

        for c in df.columns:
            if c != target:
                df[c] = pd.to_numeric(df[c], errors="coerce")

        os.makedirs(os.path.dirname(self.config.cleaned_data), exist_ok=True)
        df.to_csv(self.config.cleaned_data, index=False)
        logger.info(f"Saved cleaned dataset → {self.config.cleaned_data}")


    def train_test_split(self):
        data = pd.read_csv(self.config.cleaned_data)

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info("Data Splitted into training and testing sets")
        logger.info(f"train set shape {train.shape}")
        logger.info(f"test set shape {test.shape}")

