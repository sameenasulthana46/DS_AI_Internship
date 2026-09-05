from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import pandas as pd

# Sample data
data = {
    'Temperature': [30, 25, 20, 35, 28],
    'Appliances': [8, 5, 4, 10, 7],
    'Time': ['Afternoon', 'Morning', 'Night', 'Evening', 'Afternoon'],
    'Previous_Usage': [12, 10, 8, 15, 13],
    'Consumption': [15, 11, 9, 18, 14]
}

df = pd.DataFrame(data)

# Convert categorical data to numerical
encoder = LabelEncoder()
df['Time'] = encoder.fit_transform(df['Time'])

# Features and target
X = df[['Temperature', 'Appliances', 'Time', 'Previous_Usage']]
y = df['Consumption']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

print("Predicted Consumption:", predictions)