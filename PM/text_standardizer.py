Q1 Handling 40% Missing Income
If a DataFrame has 1M rows and 40% of the income column is missing, the first step is
to understand why the values are missing. If the missingness is random and the
column is important for analysis, dropping 40% of rows would cause significant data
loss, so filling would usually be preferable.
I would examine the distribution of income and check correlations with other variables
such as age, job type, or location. If the distribution contains strong outliers, I would use
the median instead of the mean because the median is more robust to extreme values.
Another option is group-based imputation, for example filling income based on the
median income per city or occupation.
Dropping rows would only be appropriate if the column is not important for analysis or if
the missing values occur together with many other missing fields, making the rows
unreliable.
For machine learning tasks, I might also consider advanced imputation techniques
such as KNN imputation or regression models.
The final decision depends on business context, importance of the column, and
missing data pattern.
Q2 standardize_column()
import pandas as pd
import re
def standardize_column(series: pd.Series):
 cleaned = (
 series
 .astype(str)
 .str.strip()
 .str.lower()
 .str.replace(r"\s+", " ", regex=True)
 .str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)
 )
 return cleaned
test = pd.Series([
 " Hello World!! ",
 " NEW YORK ",
 "san--francisco",
 " MUMBAI "
])
print(standardize_column(test))
Q3 Debugged Code
import pandas as pd
df = pd.DataFrame({
 "price": ["1,500", "2000", "N/A", "3,200", "abc"],
 "category": [" Electronics ", "CLOTHING", "electronics", " Books", ""],
 "date": ["15/03/2024", "2024-07-01", "22-Nov-2024", "01/10/2024", None],
})
# Fix 1: Replace hidden NaN markers
df.replace(["N/A", ""], pd.NA, inplace=True)
# Remove commas
df["price"] = df["price"].str.replace(",", "")
# Convert to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
# Fix 2: Use & instead of and
clean = df[(df["price"] > 1000) & (df["category"].notna())]
# Fix 3: Handle NaN in str operations
electronics = df[df["category"].str.contains("electronics", case=False, na=False)]
# Fix 4: Handle mixed date formats
df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
