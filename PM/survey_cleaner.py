import pandas as pd
import numpy as np
import json
np.random.seed(42)
names = ["Alice", "Bob", "Charlie", "David", "Emma"]
cities = ["New York", "Mumbai", "London", "Berlin", "Tokyo"]
data = {
 "name": np.random.choice(names, 60),
 "age": np.random.choice([25, 30, 35, None, -5, 200], 60),
 "city": np.random.choice(cities + [" mumbai ", "NEW YORK", ""], 60),
 "rating": np.random.choice([1,2,3,4,5,None], 60),
 "income": np.random.choice([50000,60000,70000,"N/A",""], 60),
 "feedback": np.random.choice(["Good", "bad", " Excellent ", None], 60),
 "date": np.random.choice(["2024-01-10","15/02/2024","22-Nov-2024",None], 60),
 "satisfaction": np.random.choice(["yes","No","YES"," no "], 60)
}
df = pd.DataFrame(data)
df = pd.concat([df, df.iloc[:5]], ignore_index=True)
def detect_issues(df: pd.DataFrame) -> dict:
 report = {}
 report["total_rows"] = len(df)
 report["total_missing"] = df.isna().sum().sum()
 report["missing_per_column"] = df.isna().sum().to_dict()
 report["duplicate_count"] = df.duplicated().sum()
 report["wrong_types"] = {
 col: str(dtype) for col, dtype in df.dtypes.items()
 }
 report["invalid_values"] = {
 "age_negative": int((df["age"] < 0).sum()),
 "age_too_high": int((df["age"] > 120).sum())
 }
 return report
def clean_data(df: pd.DataFrame):
 df.replace(["N/A", "", "None", "null"], np.nan, inplace=True)
 df["income"] = pd.to_numeric(df["income"], errors="coerce")
 df["age"] = pd.to_numeric(df["age"], errors="coerce")
 df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = np.nan
 text_cols = ["name", "city", "feedback", "satisfaction"]
 for col in text_cols:
 df[col] = (
 df[col]
 .astype(str)
 .str.strip()
 .str.lower()
 )
 df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
 df["age"].fillna(df["age"].median(), inplace=True)
 df["income"].fillna(df["income"].median(), inplace=True)
 df["city"].fillna("unknown", inplace=True)
 df["feedback"].fillna("no feedback", inplace=True)
 df.dropna(subset=["date"], inplace=True)
 df.drop_duplicates(inplace=True)
 return df
def dataset_stats(df):
 return {
 "rows": df.shape[0],
 "nulls": int(df.isnull().sum().sum()),
 "memory_mb": float(df.memory_usage(deep=True).sum() / 1e6),
 "dtypes": df.dtypes.astype(str).to_dict()
 }
before_stats = dataset_stats(df)
report = detect_issues(df)
clean_df = clean_data(df)
after_stats = dataset_stats(clean_df)
print("Before Cleaning:", before_stats)
print("After Cleaning:", after_stats)
clean_df.to_csv("cleaned_survey.csv", index=False)
with open("data_quality_report.json", "w") as f:
 json.dump(report, f, indent=4)
print("Cleaning pipeline completed.")
