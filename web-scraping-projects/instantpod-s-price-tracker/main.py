import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
EMAIL = input("Enter Email: ")

MY_EMAIL = os.getenv("EMAIL")
API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")

# Send a GET request to the URL to fetch the webpage content
response = requests.get(url="https://appbrewery.github.io/instant_pot/")

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the price of the product (assumes price is in a span with class "a-offscreen")
price = soup.find(name="span", class_="a-offscreen").getText()

# Extract the product name (assumes product name is in a span with id "productTitle")
name = soup.find(name="span", id="productTitle").getText()

# Clean up the product name by splitting and removing excess whitespace
names_list = name.split("\n")
product_name = " ".join([word.strip() for word in names_list])

# Convert the price from a string (e.g., "$99.99") to a float for comparison
price = float(price.replace("$", ""))
print(price)  # Debugging: Print the extracted price


def send_email():
    """
    Sends an email notification if the product price is below the specified threshold.
    """
    global product_name, price
    # Email credentials (password and sender email)
    password = PASSWORD  # This should be stored securely in real applications
    email = MY_EMAIL

    print("Im here")  # Debugging: Confirm the function is called

    # Set up the SMTP connection for sending the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection with TLS
        connection.login(user=email, password=password)  # Log in to the email account
        # Send an email with the product name and price
        connection.sendmail(
            from_addr=email,
            to_addrs= EMAIL,  # Recipient email
            msg=f"subject: price dropped\n\n{product_name}, 10 programs is now ${price}".encode('utf-8')
        )


# Check if the product price is below the threshold of $100
if price < 100:
    send_email()  # Call the function to send an email notification
