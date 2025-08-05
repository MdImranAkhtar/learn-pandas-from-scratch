import pandas as pd

# Load a CSV file (replace with your file path)
# df = pd.read_csv('data/your_file.csv')

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Kolkata']
}

df = pd.DataFrame(data)

print("Sample DataFrame:")
print(df)
