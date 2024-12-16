import smtplib  # Library to send emails using SMTP
import datetime as dt  # Library to work with dates and times
import random  # Library to generate random values
import pandas  # Library to work with CSV files
from dotenv import load_dotenv
import os
load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")

# Reading a CSV file that contains details about people's birthdays (name, email, month, day)
peps_details = pandas.read_csv("birthdays.csv")
index = 0  # Initialize index to track which person's birthday to check


def get_letter(name, email):
    """
    This function selects a random birthday letter template, replaces the placeholder with the name of the person,
    and sends the letter to their email.
    """
    global index
    index += 1  # Increment the index to move to the next person

    # List of available letter templates
    file_names = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

    # Open a random letter template, read the content, and replace [NAME] with the recipient's name
    with open(file=f"letter_templates/{random.choice(file_names)}", mode="r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)  # Replace [NAME] with actual name

    # Send the email with the birthday letter
    send_email(letter, email)


def send_email(letter, email):
    """
    This function sends an email with the given letter content to the specified email address.
    """
    my_email = MY_EMAIL  # Your email address (sender)
    password = PASSWORD  # Your email password (use environment variables for security in real cases)

    # Establish a connection to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Start TLS encryption for secure communication
        connection.login(user=my_email, password=password)  # Log in with your email credentials

        # Send the email with a subject and the letter content
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"subject:Happy Birthday Letter\n\n{letter}")

    # After sending the email, check for the next birthday to send
    checking_day()


def checking_day():
    """
    This function checks if today matches the birthday of anyone in the list.
    If it's someone's birthday today, it sends them a birthday letter.
    """
    global index
    # Check if there are more people to process in the CSV file
    if index < peps_details.name.count():
        # Check if today's date matches the person's birthday (month and day)
        if peps_details.iloc[index]["month"] == dt.datetime.now().month and peps_details.iloc[index][
            "day"] == dt.datetime.now().day:
            # If it's their birthday, send them a birthday letter
            get_letter(name=peps_details.iloc[index]["name"], email=peps_details.iloc[index]["email"])


# Start the process by checking if today is someone's birthday and sending them a letter
checking_day()


