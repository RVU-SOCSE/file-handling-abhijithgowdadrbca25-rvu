import pandas as pd
import csv
file='Data.csv'
df=pd.read_csv(file)
print("--- First 2 Rows ---")
print(df.head(2))
