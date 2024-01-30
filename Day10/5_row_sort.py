import pandas as pd

df = pd.read_csv("student_ds.csv")

sorted_df = df[df['age'] > 18]

print("sorted  DF:")
print(sorted_df)
