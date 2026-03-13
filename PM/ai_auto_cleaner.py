def auto_clean_dataframe(df):
 summary = {}
 original_rows = len(df)
 df.replace(["N/A", "", "null", "None"], pd.NA, inplace=True)
 for col in df.columns:
 if df[col].dtype == "object":
 # try numeric conversion
 df[col] = pd.to_numeric(df[col], errors="ignore")
 # try datetime conversion
 df[col] = pd.to_datetime(df[col], errors="ignore")
 if df[col].dtype == "object":
 df[col] = df[col].str.strip().str.lower()
 duplicates = df.duplicated().sum()
 df.drop_duplicates(inplace=True)
 summary["rows_removed"] = int(original_rows - len(df))
 summary["duplicates_removed"] = int(duplicates)
 return df, summary
