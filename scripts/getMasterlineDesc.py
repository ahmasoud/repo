import pandas as pd

# Replace '8.xls' with the actual path to your Excel file if it's not in the current directory
excel_file = '8.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# Print column names
value = df.loc[25, 0]
print(value)

