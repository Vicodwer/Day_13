import pandas as pd
jan = pd.DataFrame({
 "product": ["Laptop", "Phone", "Headphones"],
 "units_sold": [10, 25, 40],
 "price": [55000, 30000, 2500]
})
feb = pd.DataFrame({
 "product": ["Laptop", "Phone", "Headphones"],
 "units_sold": [12, 20, 35],
 "price": [55000, 30000, 2500]
})
mar = pd.DataFrame({
 "product": ["Laptop", "Phone", "Headphones"],
 "units_sold": [15, 28, 45],
 "price": [55000, 30000, 2500]
})
months = {"January": jan, "February": feb, "March": mar}
summary = []
for month, df in months.items():
 df["revenue"] = df["units_sold"] * df["price"]
 total_revenue = df["revenue"].sum()
 avg_order_value = df["revenue"].mean()
 top_product = df.loc[df["units_sold"].idxmax(), "product"]
 summary.append({
 "month": month,
 "total_revenue": total_revenue,
 "avg_order_value": avg_order_value,
 "top_product": top_product
 })
summary_df = pd.DataFrame(summary).set_index("month")
print(summary_df)
high_sales = jan.query("units_sold > 20")
largest_sales = jan.nlargest(1, "units_sold")
smallest_sales = jan.nsmallest(1, "units_sold")
print(largest_sales)
print(smallest_sales)
