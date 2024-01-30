import pandas as pd

df = pd.read_csv('student_ds.csv')
print("initial df")
print(df.head())


df['defaulter'] = df['goout'] + df['absences'] 

print("updated column:")
print(df.head())
