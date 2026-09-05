import pandas as pd

# Create a Series with names and missing values
names = pd.Series(["ALICE", "Bob", None, "CHARLIE", "David", None, "EMMA"])

print("Original Series:")
print(names)

# Detect missing values
print("\nMissing values:")
print(names.isnull())

# Fill missing values
names = names.fillna("Unknown")

print("\nAfter filling missing values:")
print(names)

# Convert all names to lowercase
names = names.str.lower()

print("\nNames in lowercase:")
print(names)

# Filter names containing the letter 'a'
result = names[names.str.contains("a")]

print("\nNames containing letter 'a':")
print(result)