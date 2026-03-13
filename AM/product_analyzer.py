import pandas as pd
products = [
 {"name": "Laptop", "category": "Electronics", "price": 55000, "stock": 15,
"rating": 4.5, "num_reviews": 250},
 {"name": "Smartphone", "category": "Electronics", "price": 30000, "stock":
30, "rating": 4.3, "num_reviews": 400},
 {"name": "Headphones", "category": "Electronics", "price": 2500, "stock":
50, "rating": 4.1, "num_reviews": 180},
 {"name": "Bluetooth Speaker", "category": "Electronics", "price": 3500,
"stock": 25, "rating": 4.2, "num_reviews": 120},
 {"name": "T-Shirt", "category": "Clothing", "price": 800, "stock": 100,
"rating": 4.0, "num_reviews": 90},
 {"name": "Jeans", "category": "Clothing", "price": 1800, "stock": 60,
"rating": 4.3, "num_reviews": 110},
 {"name": "Jacket", "category": "Clothing", "price": 3500, "stock": 40,
"rating": 4.6, "num_reviews": 210},
 {"name": "Sneakers", "category": "Clothing", "price": 4000, "stock": 45,
"rating": 4.4, "num_reviews": 150},
 {"name": "Notebook", "category": "Books", "price": 500, "stock": 200,
"rating": 4.1, "num_reviews": 50},
 {"name": "Python Programming", "category": "Books", "price": 900, "stock":
80, "rating": 4.7, "num_reviews": 300},
 {"name": "Data Science Handbook", "category": "Books", "price": 1200,
"stock": 60, "rating": 4.5, "num_reviews": 220},
 {"name": "Cookbook", "category": "Books", "price": 700, "stock": 70,
"rating": 4.2, "num_reviews": 95},
 {"name": "Sofa", "category": "Home", "price": 15000, "stock": 10, "rating":
4.4, "num_reviews": 130},
 {"name": "Dining Table", "category": "Home", "price": 20000, "stock": 8,
"rating": 4.6, "num_reviews": 160},
 {"name": "Lamp", "category": "Home", "price": 1200, "stock": 90, "rating":
4.0, "num_reviews": 70},
 {"name": "Curtains", "category": "Home", "price": 1500, "stock": 85,
"rating": 4.3, "num_reviews": 105},
 {"name": "Smartwatch", "category": "Electronics", "price": 7000, "stock": 35,
"rating": 4.2, "num_reviews": 190},
 {"name": "Tablet", "category": "Electronics", "price": 20000, "stock": 20,
"rating": 4.4, "num_reviews": 170},
 {"name": "Microwave", "category": "Home", "price": 8000, "stock": 18,
"rating": 4.3, "num_reviews": 145},
 {"name": "Backpack", "category": "Clothing", "price": 1200, "stock": 75,
"rating": 4.2, "num_reviews": 115},
]
df = pd.DataFrame(products)
print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())
print("\nFirst 5 rows:")
print(df.head())
electronics = df.loc[df["category"] == "Electronics"]
# b) Rating > 4 and price < 5000
high_rated_affordable = df.loc[(df["rating"] > 4.0) & (df["price"] < 5000)]
df.loc[df["name"] == "Laptop", "stock"] = 12
first_five = df.iloc[:5]
last_five = df.iloc[-5:]
every_other = df.iloc[::2]
subset = df.iloc[10:16, 0:4]
budget_products = df[df["price"] < 1000]
premium_products = df[df["price"] > 10000]
popular_products = df[(df["num_reviews"] > 100) & (df["rating"] > 4.0)]
dfs =
{
 "budget_products": budget_products,
 "premium_products": premium_products,
 "popular_products": popular_products
}
for name, dataframe in dfs.items():
 dataframe.to_csv(f"{name}.csv", index=False)
print("CSV files exported successfully.")
