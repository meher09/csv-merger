import pandas as pd
first_file = input("Enter First File Name: ")
second_file = input("Enter second File Name: ")
df1 = pd.read_csv(first_file)
df2 = pd.read_csv(second_file)
common_column = input("Enter the common column name: ")
merged = pd.merge(df1, df2, on=common_column)
merged.to_csv('merged_file.csv', index=False)
