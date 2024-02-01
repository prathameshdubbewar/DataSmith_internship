import pandas as pd

csv1 = pd.read_csv("student_ds.csv")
csv2 = pd.read_csv("student_ds.csv")

# consider student id as common column
merged_df = pd.merge(csv1, csv2, on='student id', how='inner')

print("merged df:")
print(merged_df)
