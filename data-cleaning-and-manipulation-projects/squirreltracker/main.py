# Import the pandas library to handle data manipulation
import pandas

# Read the CSV file into a pandas DataFrame
# The file contains squirrel data, including their fur color and other attributes
data_frame = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241118.csv")

# Count the number of squirrels with "Gray" fur color
gray = data_frame[data_frame["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()

# Count the number of squirrels with "Black" fur color
black = data_frame[data_frame["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()

# Count the number of squirrels with "Cinnamon" fur color
cinnamon = data_frame[data_frame["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()

# Create a dictionary containing the fur colors and their respective counts
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],  # List of fur colors
    "Count": [gray, black, cinnamon]  # List of counts corresponding to each fur color
}

# Convert the dictionary into a pandas DataFrame
color_count = pandas.DataFrame(data_dict)

# Save the DataFrame to a new CSV file, containing the fur color counts
color_count.to_csv("squirrel_count.csv")
