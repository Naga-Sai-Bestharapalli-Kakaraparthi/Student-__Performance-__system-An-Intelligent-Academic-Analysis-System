import pandas as pd
from src.etl_pipeline import StudentDataETLPipeline

def test_etl_transform():
    # Step 1: Create fake/mock input data with a missing value (None)
    dummy_data = pd.DataFrame({
        "study_hours": [5.0, None, 10.0],
        "attendance": [80, 90, 70]
    })
    
    # Step 2: Pass fake data through the transform function
    pipeline = StudentDataETLPipeline(data_path="dummy.csv")
    cleaned_df = pipeline.transform(dummy_data)
    
    # Step 3: Assert (verify) expected outputs
    # Verifies null values were removed
    assert cleaned_df["study_hours"].isnull().sum() == 0  
    # Verifies the feature column was generated
    assert "study_hours_normalized" in cleaned_df.columns
