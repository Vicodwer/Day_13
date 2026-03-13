Q1 Answer
.loc[] vs .iloc[]
Feature .loc .iloc
Type Label-based Position-based
Uses Index labels Integer positions
Slice behavior Inclusive Exclusive
Example:
df.loc[0:3]
Returns rows 0,1,2,3 because .loc is inclusive.
df.iloc[0:3]
Returns rows 0,1,2 because .iloc excludes the end index.
If index is:
a b c d e
Then
df.loc['a':'c']
returns a,b,c
but
df.iloc[0:3]
still returns a,b,c because it uses position.
Q2 analyze_csv function
import pandas as pd
def analyze_csv(filepath: str) -> dict:
 df = pd.read_csv(filepath)
 print("Shape:", df.shape)
 print("\nInfo:")
 print(df.info())
 print("\nDescribe:")
 print(df.describe())
 numeric_cols = df.select_dtypes(include="number").columns.tolist()
 categorical_cols = df.select_dtypes(exclude="number").columns.tolist()
 result = {
 "num_rows": df.shape[0],
 "num_cols": df.shape[1],
 "numeric_cols": numeric_cols,
 "categorical_cols": categorical_cols,
 "null_counts": df.isnull().sum().to_dict(),
 "memory_mb": df.memory_usage(deep=True).sum() / 1e6
 }
 return result
Q3 Debugged Code
import pandas as pd
df = pd.DataFrame({
 "name": ["Alice", "Bob", "Charlie"],
 "age": [25, 30, 35],
 "salary": [50000, 60000, 70000]
})
# Fix 1: Use & and parentheses
high_earners = df[(df["age"] > 25) & (df["salary"] > 55000)]
# Fix 2: Use loc instead of chained indexing
df.loc[0, "age"] = 26
# Fix 3: iloc end is exclusive
first_three = df.iloc[0:3]
print(f"Got {len(first_three)} rows")
