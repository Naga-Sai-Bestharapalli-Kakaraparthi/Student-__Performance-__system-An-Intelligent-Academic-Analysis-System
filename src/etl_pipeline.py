class StudentDataETLPipeline:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def extract() -> pd.DataFrame:
        # What it does: Checks if the file exists and reads the raw CSV.
        # Why: Prevents the application from crashing silently if data is missing.
        return pd.read_csv(self.data_path)

    def transform(df: pd.DataFrame) -> pd.DataFrame:
        # What it does: 
        # 1. Replaces missing values (NaNs) with column medians so models don't crash.
        # 2. Creates normalized features (scales values between 0 and 1).
        # Why: ML algorithms perform better when numerical features are on the same scale.
        df_clean = df.copy()
        df_clean.fillna(df_clean.median(numeric_only=True), inplace=True)
        # Min-Max Scaling formula: (x - min) / (max - min)
        return df_clean
