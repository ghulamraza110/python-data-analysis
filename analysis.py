import pandas as pd

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}

df = pd.DataFrame(data)

# Display basic statistics
print("Basic Statistics:\n", df.describe())

# Save to CSV
df.to_csv("sample_data.csv", index=False)
print("Data saved to sample_data.csv")
