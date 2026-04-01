import pandas as pd

file_path = 'Data.csv'
df = pd.read_csv(file_path)

# Get the number of rows and columns using .shape
rows, columns = df.shape

print(f"Total number of rows: {rows}")
print(f"Total number of columns: {columns}")
