Prompt Used
Write a Python function that takes a Pandas DataFrame and generates an
automated data quality report including:
shape, dtypes, missing values percentage, duplicate rows, unique value counts
per column, and basic stats.
Return the report as a dictionary and also print a formatted summary.
AI Generated Function
import pandas as pd
def data_quality_report(df):
 report = {}
 report["shape"] = df.shape
 report["dtypes"] = df.dtypes.astype(str).to_dict()
 report["missing_percent"] = (df.isnull().mean() * 100).to_dict()
 report["duplicates"] = df.duplicated().sum()
 report["unique_values"] = df.nunique().to_dict()
 report["stats"] = df.describe().to_dict()
 print("DATA QUALITY REPORT")
 print("Shape:", report["shape"])
 print("Duplicates:", report["duplicates"])
 return report
Test Example
clean_df = pd.DataFrame({
 "A": [1,2,3],
 "B": ["x","y","z"]
})
messy_df = pd.DataFrame({
 "A": [1,None,3],
 "B": ["x","x","x"]
})
data_quality_report(clean_df)
data_quality_report(messy_df)
