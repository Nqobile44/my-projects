from tkinter import *  # Import the tkinter module for GUI development

def calculate_miles():
    """This function calculates miles to kilometers and displays the result."""
    miles = user_miles.get()  # Get the value entered by the user in the input field
    result = int(miles) * 1.60934  # Convert miles to kilometers (1 mile = 1.60934 km)
    result_total.config(text=str(round(result, 2)))  # Update the result label with the converted value, rounded to 2 decimal places

# UI Setup
window = Tk()  # Create the main window for the application
window.minsize(width=300, height=100)  # Set the minimum size of the window
window.title("Mile to Km Converter")  # Set the title of the window
window.config(padx=30, pady=30)  # Add padding around the window's content

# Entry field for user input (miles)
user_miles = Entry()  # Create an input field where the user can enter miles
user_miles.grid(column=2, row=1)  # Place the input field in the grid (column 2, row 1)
user_miles.insert(END, "0")  # Insert a default value of "0" in the input field
user_miles.focus()  # Set the focus on the input field when the application starts

# Label for "Miles" text next to the input field
miles_label = Label(window, text="Miles")
miles_label.grid(column=3, row=1)  # Place the label in the grid (column 3, row 1)

# Label for the phrase "Is equal to" (between the input and result)
result_label = Label(window, text="Is equal to")
result_label.grid(column=1, row=2)  # Place the label in the grid (column 1, row 2)

# Label to display the calculated result (km)
result_total = Label(window, text="0")  # Initial result text is "0"
result_total.grid(column=2, row=2)  # Place the label in the grid (column 2, row 2)

# Label for "Km" text next to the result
result_id = Label(window, text="Km")
result_id.grid(column=3, row=2)  # Place the label in the grid (column 3, row 2)

# Button to trigger the calculation when clicked
calculate_button = Button(text="Calculate", command=calculate_miles)
calculate_button.grid(column=2, row=3)  # Place the button in the grid (column 2, row 3)

# Start the tkinter event loop to keep the window running
window.mainloop()
