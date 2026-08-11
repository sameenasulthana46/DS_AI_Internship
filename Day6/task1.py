import numpy as np

# Daily sales of 3 products for 4 days
sales = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40],
    [25, 35, 45]
])

print("Daily Product Sales:")
print(sales)

# Product-wise analysis (axis=0)
print("\nProduct-wise Analysis:")
print("Mean:", np.mean(sales, axis=0))
print("Median:", np.median(sales, axis=0))
print("Variance:", np.var(sales, axis=0))
print("Standard Deviation:", np.std(sales, axis=0))

# Day-wise analysis (axis=1)
print("\nDay-wise Analysis:")
print("Mean:", np.mean(sales, axis=1))
print("Median:", np.median(sales, axis=1))
print("Variance:", np.var(sales, axis=1))
print("Standard Deviation:", np.std(sales, axis=1))