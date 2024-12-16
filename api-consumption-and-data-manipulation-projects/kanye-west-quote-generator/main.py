# Importing necessary libraries for GUI (Tkinter) and making HTTP requests (requests)
from tkinter import *
import requests


# Function to get a quote from the Kanye West quote API and display it
def api_displayer():
    """It gets a quote from the API and displays it to the user"""
    # Send a GET request to the Kanye West quote API
    response = requests.get(url="https://api.kanye.rest/")

    # Update the text of the quote displayed on the canvas with the quote from the API response
    canvas.itemconfig(quote, text=response.json().get("quote"))


# Create the main window for the Tkinter application
window = Tk()
# Configure the window with padding on all sides
window.config(pady=20, padx=20)

# Create a Canvas widget to hold the background and text
canvas = Canvas(window, width=300, height=414)
# Load and set the background image for the canvas
image = PhotoImage(file="background.png")
canvas.create_image(150, 215, image=image)  # Set the position of the background image
# Create the text that will show the quote from the API (initially empty)
quote = canvas.create_text(150, 220, text="Kanye Quotes Goes Here", width=250, fill="white", font=("ariel", 30))
canvas.pack()  # Display the canvas in the window

# Load the image for the Kanye button
kanye_image = PhotoImage(file="kanye.png")
# Create a button with the Kanye image, which calls the 'api_displayer' function when clicked
kanye_button = Button(image=kanye_image, command=api_displayer)
kanye_button.pack()  # Display the button

# Start the Tkinter event loop to keep the window open
window.mainloop()
