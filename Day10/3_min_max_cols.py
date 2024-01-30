import pandas as pd


df = pd.read_csv('student_ds.csv')


for column in df.columns:

    try:
        num_values = pd.to_numeric(df[column])

        max_value = num_values.max()
        min_value = num_values.min()

        print(f"column: {column}")
        print(f"max value: {max_value}")
        print(f"Min value: {min_value}")
        print()
    except :
        
        print(f"Column '{column}' has no num values.")
        print()

