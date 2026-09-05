import pandas as pd

# Read the CSV file
data = pd.read_csv("student.csv")

# Display original dataset
print("Original Dataset:")
print(data)

# Find shape
print("\nOriginal Shape:")
print(data.shape)

# Identify missing values
print("\nMissing Values:")
print(data.isnull())

# Count missing values
print("\nCount of Missing Values:")
print(data.isnull().sum())

# Detect duplicate rows
print("\nNumber of Duplicate Rows:")
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(data)

# Handle missing values using column mean
data["Maths"] = data["Maths"].fillna(data["Maths"].mean()).astype(int)
data["Science"] = data["Science"].fillna(data["Science"].mean()).astype(int)
data["English"] = data["English"].fillna(data["English"].mean()).astype(int)

# Check missing values after handling
print("\nMissing Values After Handling:")
print(data.isnull().sum())

# Display cleaned dataset
print("\nCleaned Dataset:")
print(data)

# Find final shape
print("\nCleaned Dataset Shape:")
print(data.shape)

print(data.iloc[0])