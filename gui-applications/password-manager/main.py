from tkinter import *  # Import the tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox for showing alerts and messages
import random  # Import random module for password generation
import pyperclip  # Import pyperclip for copying text to the clipboard
import json  # Import json module for managing data in a JSON file


# ---------------------------- SEARCH DATA --------------------------------------- #
def find_password():
    """Search for saved password details for a website in the data file."""
    website_name = website_input.get()  # Get the website name entered by the user
    try:
        with open(file="data.json", mode="r") as data_file:  # Open the JSON file in read mode
            data = json.load(fp=data_file)  # Load the data from the JSON file

            # Display the email and password for the website in a message box
            messagebox.showinfo(title=website_name,
                                message=f"Email: {data[website_name]['email']}\nPassword: {data[website_name]['password']}")
    except FileNotFoundError:
        # Show an error message if the data file doesn't exist
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        # Show an error message if the website details are not found
        messagebox.showerror(title="Error", message="No Details for the website exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator_password():
    """Generate a strong random password and copy it to the clipboard."""
    # Define possible characters for the password
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    # Generate a list of random characters for the password
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]  # Random letters
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]  # Random symbols
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]  # Random numbers

    random.shuffle(password_list)  # Shuffle the characters for randomness

    password = "".join(password_list)  # Combine the characters into a string

    # Update the password input field with the generated password
    password_input.delete(0, END)
    password_input.insert(END, password)

    # Copy the generated password to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save the entered website, email/username, and password to a JSON file."""
    website_name = website_input.get()  # Get the website name from the input
    email_username = email_username_input.get()  # Get the email/username from the input
    password = password_input.get()  # Get the password from the input

    # Check if any of the fields are empty
    if len(website_name) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Confirm with the user before saving
        is_ok = messagebox.askokcancel(
            title=website_name,
            message=f"These are the details entered: \nEmail: {email_username}\nPassword: {password}\nIs it ok to save?"
        )
        if is_ok:
            new_data = {
                website_name: {
                    "email": email_username,
                    "password": password,
                }
            }
            try:
                with open(file="data.json", mode="r") as data_file:  # Try to open the JSON file in read mode
                    old_data = json.load(fp=data_file)  # Load existing data
                    old_data.update(new_data)  # Update with new data
            except FileNotFoundError:
                # If file not found, create a new file and save the data
                with open(file="data.json", mode="w") as data_file:
                    json.dump(obj=new_data, fp=data_file, indent=4)
            else:
                # Save the updated data back to the file
                with open(file="data.json", mode="w") as data_file:
                    json.dump(obj=old_data, fp=data_file, indent=4)
            finally:
                # Clear the input fields and refocus on the website input field
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
                messagebox.showinfo(title="Details Saved", message="Details have been successfully saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create the main window for the application
window.title("Password Manager")  # Set the title of the window
window.config(padx=50, pady=50)  # Add padding around the window content

# Add a canvas to display a logo image
canvas = Canvas(window, width=200, height=200)
image = PhotoImage(file="logo.png")  # Load the logo image
canvas.create_image(100, 89, image=image)  # Place the image at the center of the canvas
canvas.grid(column=1, row=0)

# Label and input for website
website_id = Label(window, text="Website:")
website_id.grid(column=0, row=1)
website_input = Entry(window, width=17)
website_input.grid(column=1, row=1)
website_input.focus()  # Set focus to the website input field

# Button to search for website details
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

# Label and input for email/username
email_username_id = Label(window, text="Email/Username:")
email_username_id.grid(column=0, row=2)
email_username_input = Entry(window, width=35)
email_username_input.grid(column=1, row=2, columnspan=2)

# Label and input for password
password_id = Label(window, text="Password:")
password_id.grid(column=0, row=3)
password_input = Entry(width=17)
password_input.grid(column=1, row=3)

# Button to generate a new password
gen_button = Button(text="Generate Password", command=generator_password)
gen_button.grid(column=2, row=3)

# Button to add/save the details
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Start the tkinter event loop to keep the application running
window.mainloop()
