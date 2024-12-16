from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up options for the Edge WebDriver to keep the browser open after the script finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(name="detach", value=True)

# Initialize the Edge WebDriver with the specified options
driver = webdriver.Edge(options=edge_options)

# Navigate to the Python.org homepage
driver.get("https://www.python.org/")

# Find elements with the class name "shrubbery" which contain the events section
big_step = driver.find_elements(by=By.CLASS_NAME, value="shrubbery")

# Extract the text from each element in the list `big_step`
toxic_elements = [element.text for element in big_step]

# Select the text related to upcoming events, skipping irrelevant information
# Split by new lines and remove the first two elements to focus on the event data
upcoming_events = toxic_elements[1].split("\n")[2:]

# Extract dates from the upcoming events list (even-indexed items)
data_values = [upcoming_events[item] for item in range(0, len(upcoming_events), 2)]

# Extract event names from the upcoming events list (odd-indexed items)
name_values = [upcoming_events[item] for item in range(1, len(upcoming_events), 2)]

# Create a dictionary where each key is an index, and the value is another dictionary
# containing the event "time" (date) and "name" (event name)
dict_result = {data_values.index(item): {"time": item} for item in data_values}

# Update the dictionary to add "name" for each event
for item in name_values:
    dict_result[name_values.index(item)].update({"name": item})

# Print the final dictionary containing all upcoming events with their times and names
print(dict_result)

# Close the WebDriver instance
driver.quit()

