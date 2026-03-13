import pandas as pd
from scipy.stats import skew
def data_profiler(df: pd.DataFrame):
 profile = {}
 for col in df.columns:
 col_data = {}
 col_data["dtype"] = str(df[col].dtype)
 col_data["unique_count"] = df[col].nunique()
 col_data["null_count"] = int(df[col].isna().sum())
 col_data["null_percent"] = float(df[col].isna().mean() * 100)
 col_data["top_values"] = df[col].value_counts().head(5).to_dict()
 if pd.api.types.is_numeric_dtype(df[col]):
 col_data["min"] = float(df[col].min())
 col_data["max"] = float(df[col].max())
 col_data["mean"] = float(df[col].mean())
 col_data["median"] = float(df[col].median())
 col_data["std"] = float(df[col].std())
 col_data["skewness"] = float(skew(df[col].dropna()))
 else:
 lengths = df[col].dropna().astype(str).str.len()
 col_data["avg_length"] = float(lengths.mean())
 col_data["min_length"] = int(lengths.min())
 col_data["max_length"] = int(lengths.max())
 issues = []
 if df[col].nunique() == 1:
 issues.append("single_value_column")
 if df[col].nunique() > 0.9 * len(df):
 issues.append("high_cardinality")
 if pd.api.types.is_numeric_dtype(df[col]):
 outliers = ((df[col] - df[col].mean()).abs() > 3 * df[col].std()).sum()
 if outliers > 0:
 issues.append("potential_outliers")
 col_data["issues"] = issues
 profile[col] = col_data
 print("DATA PROFILE SUMMARY")
 print("Shape:", df.shape)
 return profile
