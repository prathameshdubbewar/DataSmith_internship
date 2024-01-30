import pandas as pd

df = pd.read_csv('student_ds.csv')


grouped_mean = df.groupby('goout')['absences'].mean()


print(grouped_mean)
