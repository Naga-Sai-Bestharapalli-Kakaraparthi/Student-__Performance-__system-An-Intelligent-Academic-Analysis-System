import pandas as pd
import pytest
from src.etl_pipeline import StudentDataETLPipeline

def test_etl_transform_shape():
    # Mock sample dataset
    dummy_data = pd.DataFrame({
        "study_hours": [5.0, None, 10.0],
        "attendance": [80, 90, 70]
    })
    
    pipeline = StudentDataETLPipeline(data_path="dummy.csv")
    cleaned_df = pipeline.transform(dummy_data)
    
    # Assert missing values were filled
    assert cleaned_df["study_hours"].isnull().sum() == 0
    # Assert normalized feature columns were generated
    assert "study_hours_normalized" in cleaned_df.columns
