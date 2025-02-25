from json_extract import ExtractFromJ
from data_import import DataImport
from data_import import open_file

extract_from_json = ExtractFromJ()
data = extract_from_json.data
columns = list(data.get("shoppingList").get("groceries")[0].keys())

data_import = DataImport(list(data.keys())[0], columns, data["shoppingList"])
data_import.extract()
data_import.save_data()
open_file()