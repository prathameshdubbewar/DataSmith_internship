import pandas as pd

df = pd.read_csv('student_ds.csv')

numeric_columns = df.select_dtypes(include=['int', 'float'])

column_sums = numeric_columns.sum()

print("Sum of columns is:")
print(column_sums)
