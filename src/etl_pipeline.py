import os
import pandas as pd
import numpy as np
from typing import Tuple

class StudentDataETLPipeline:
    """ETL Pipeline for ingesting, cleaning, and feature-engineering student interaction data."""

    def __init__(self, data_path: str):
        self.data_path = data_path

    def extract(self) -> pd.DataFrame:
        """Extract step: Ingest raw CSV data safely."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found at {self.data_path}")
        return pd.read_csv(self.data_path)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform step: Clean missing values, encode features, and derive engagement metrics."""
        df_clean = df.copy()
        
        # Handle missing values
        df_clean.fillna(df_clean.median(numeric_only=True), inplace=True)

        # Feature Engineering: Derive aggregated engagement ratio if columns exist
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df_clean[f"{col}_normalized"] = (df_clean[col] - df_clean[col].min()) / (df_clean[col].max() - df_clean[col].min() + 1e-5)

        return df_clean

    def run(self) -> pd.DataFrame:
        """Executes full ETL process."""
        raw_df = self.extract()
        transformed_df = self.transform(raw_df)
        return transformed_df

if __name__ == "__main__":
    pipeline = StudentDataETLPipeline("student_learning_interaction_dataset.csv")
    clean_data = pipeline.run()
    print(f"Pipeline executed successfully. Processed {clean_data.shape[0]} rows and {clean_data.shape[1]} features.")
