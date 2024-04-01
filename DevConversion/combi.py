import pandas as pd
import os

dev_files_dir = r'C:\Users\Pratham\OneDrive\Desktop\Intenship\DevConversion\Sajaa 1'

dfs = []

for filename in os.listdir(dev_files_dir):
    if filename.endswith('.dev'):
        df = pd.read_csv(os.path.join(dev_files_dir, filename), delimiter='\t')
        
        df['Name'] = filename[:-4] 
        dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

excel_file_path = 'combined_data.xlsx'
combined_df.to_excel(excel_file_path, index=False)

print(f"Combined data saved to {excel_file_path}")
