import pandas as pd


df = pd.read_csv("Day10/student_ds.csv")

print("initial df:")
print(df)

transposed_df = df.transpose()

print("transpose df:")
print(transposed_df)
