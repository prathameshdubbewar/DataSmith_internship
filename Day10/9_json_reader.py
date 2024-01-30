import pandas as pd

df = pd.read_json('Day10/csvjson.json')


print(df.head())
gender_and_ages = df[['sex', 'age']]

print(gender_and_ages)
