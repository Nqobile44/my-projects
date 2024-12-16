# Import necessary libraries for sending email (smtplib) and making HTTP requests (requests)
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")


# It gets email from the user to send to.
EMAIL = input("Enter Your Email: ")

# Define API endpoint and API key for OpenWeatherMap API
api = "https://api.openweathermap.org/data/2.5/forecast"

# Latitude and Longitude coordinates for the location
lat = 30.980840
lng = -29.881890

# Parameters for the API request, including location and forecast count
para_data = {
    "lat": lat,
    "lon": lng,
    "appid": API_KEY,  # API key for authentication
    "cnt": 12  # Number of forecast data points to retrieve (12 data points)
}

# Function to send an email notification (SMS) when it will rain
def send_sms():
    """Sends an email to notify the user about rain and to bring an umbrella"""
    # Set up the connection with the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        # Log into Gmail using the provided email and password
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # Send the email with the subject and body
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=EMAIL,
            msg="Subject: Weather forecast\n\nThe weather is going to rain today. Remember to bring an umbrella."
        )
        # Optional: you can include more details in the message like the exact time of rain.

# Make a GET request to the weather API with the defined parameters
response = requests.get(url=api, params=para_data)

# Raise an error if the request was not successful
response.raise_for_status()

# Convert the JSON response into a Python dictionary
weather = response.json()

# Loop through the forecast data and check if it will rain
for day in weather.get("list"):
    # Check the weather condition ID to see if it's a rain condition
    if day.get("weather")[0].get("id") < 700:
        print("Bring an Umbrella")  # Print message for the user
        send_sms()  # Send the email notification
        break  # Exit the loop after sending the email (no need to check further)



