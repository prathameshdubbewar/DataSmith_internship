import pandas as pd
import os

# Path to the directory containing dev files
dev_files_dir = r'C:\Users\Pratham\OneDrive\Desktop\Intenship\DevConversion\Sajaa 1'

# List to store DataFrames from each dev file
dfs = []

# Iterate over each dev file in the directory
for filename in os.listdir(dev_files_dir):
    if filename.endswith('.dev'):
        # Read the dev file into a DataFrame
        df = pd.read_csv(os.path.join(dev_files_dir, filename), delimiter='\t')
        
        # Add a column of names
        df['Name'] = filename[:-4]  # Remove the '.dev' extension from the filename
        
        # Append the DataFrame to the list
        dfs.append(df)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to an Excel file
excel_file_path = 'combined_data.xlsx'
combined_df.to_excel(excel_file_path, index=False)

print(f"Combined data saved to {excel_file_path}")
