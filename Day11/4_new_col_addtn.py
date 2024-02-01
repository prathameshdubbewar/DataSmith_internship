import pandas as pd

df = pd.read_csv('books.csv')

def year_sort(year):
    if year < 1950:
        return 'Classic'
    else:
        return 'Modern'

df['category'] = df['Publication Year'].apply(year_sort)

print(df)
