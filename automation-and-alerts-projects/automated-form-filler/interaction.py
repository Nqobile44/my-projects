import time  # Importing the time module to pause the program for a specified time
from selenium import webdriver  # Importing the selenium module to control a web browser
from selenium.webdriver.common.by import By  # Importing the By class to locate elements on the web page

# Get user input for first name, last name, and email, with title case for names
first_name = input("Enter Your first name: ").title()  # Title case (e.g., John)
last_name = input("Enter Your last name: ").title()  # Title case (e.g., Doe)
email = input("Enter Your email: ")  # User's email address

# Setting up Edge options to run the browser in a detached mode (browser won't close when the script finishes)
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(name="detach", value=True)

# Initialize the Edge WebDriver with the specified options
driver = webdriver.Edge(edge_options)

# Open the specified URL (secure-retreat-92358.herokuapp.com) in the browser
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

# Find the input fields on the web page using their name attributes
first_name_input = driver.find_element(by=By.NAME, value="fName")  # First name input field
last_name_input = driver.find_element(by=By.NAME, value="lName")  # Last name input field
email_input = driver.find_element(by=By.NAME, value="email")  # Email input field

# Find the submit button using its class name
submit_button = driver.find_element(by=By.CLASS_NAME, value="btn")

# Fill in the input fields with the values provided by the user
first_name_input.send_keys(first_name)  # Type the first name into the first name field
last_name_input.send_keys(last_name)    # Type the last name into the last name field
email_input.send_keys(email)            # Type the email into the email field

# Click the submit button to submit the form
submit_button.click()

# Wait for 4 seconds to let the form submission complete
time.sleep(4)

# Close the browser after the action is complete
driver.quit()
