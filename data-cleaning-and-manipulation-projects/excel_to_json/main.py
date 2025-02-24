# Import the custom DataExtract class for reading Excel data
from data_export import DataExtract
# Import the built-in JSON module for handling JSON file operations
import json

# Initialize the DataExtract object and load Excel data
data_extract = DataExtract()
data_extract.get_columns()  # Extract column headers from the Excel file
data = data_extract.get_data()  # Extract the main data from the Excel file

# Process and clean date fields in the extracted data
for row in data:
    # Extract and format 'Start Date' by removing time information if present
    start_date =  str(row.get("Start Date")).split()[0]
    row["Start Date"] = start_date

    # Extract and format 'End Date' by removing time information if present
    end_date = str(row.get("End Date")).split()[0]
    row["End Date"] = end_date

# Insert the column headers at the beginning of the dataset for reference
data.insert(0, {"Columns": data_extract.columns})

# Save the processed data to a JSON file with proper formatting
with open("data/new_data.json", "w") as file:
    json.dump(obj=data, fp=file, indent=4)  # Write JSON with indentation for readability