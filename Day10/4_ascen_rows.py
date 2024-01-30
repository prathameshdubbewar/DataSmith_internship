import pandas as pd

def sort_df(df):
    sorted_df = df.sort_values(by=list(df.columns))
    return sorted_df


data = {
    'Name': ['A', 'C', 'B'],
    'Age': [25, 30, 28],
    'Score': [90, 85, 95]
}
df = pd.DataFrame(data)


sorted_df = sort_df(df)
print("Sorted df:")
print(sorted_df)
