import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file_path = 'table.ods'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path, header=None)

# Convert the DataFrame to a Python list matrix
python_list_matrix = df.values.tolist()

# Print the Python list matrix
print("Python List Matrix:")
for row in python_list_matrix:
    print(row)