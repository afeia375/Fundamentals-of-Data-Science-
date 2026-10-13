
import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

sales_data = df["Total"].to_numpy()

quarter_sales = np.array([
    sales_data[0:3].sum(),
    sales_data[3:6].sum(),
    sales_data[6:9].sum(),
    sales_data[9:12].sum()
])

total_sales = np.sum(quarter_sales)

percentage_increase = (
    (quarter_sales[3] - quarter_sales[0]) / quarter_sales[0]
) * 100

print("Total Annual Sales:", round(total_sales, 2))
print("First Quarter Sales:", round(quarter_sales[0], 2))
print("Fourth Quarter Sales:", round(quarter_sales[3], 2))
print("Percentage Increase:", round(percentage_increase, 2), "%")
