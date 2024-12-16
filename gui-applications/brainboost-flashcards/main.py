from tkinter import *  # Import the tkinter module for the GUI
import pandas  # Import pandas to work with CSV files
import random  # Import random module to generate random words

BACKGROUND_COLOR = "#B1DDC6"  # Set the background color for the app
word_gen = None  # Global variable to store the current word being shown
correct_words = list()  # List to store words that the user has answered correctly
data = pandas.read_csv("data/french_words.csv")  # Read data from a CSV file containing French words and their English translations

def flip_card(boolean):
    """This function flips the card and changes the background image and text."""
    canvas.itemconfig(front_image, image=back_image_card)  # Change the card to the back image
    canvas.itemconfig(title, text="English", fill="white")  # Set the title to "English" and change text color to white
    canvas.itemconfig(word, text=word_data[word_gen], fill="white")  # Show the English word on the card

# Create a dictionary to map French words to their English translations
word_data = dict()
for (index, value) in data.iterrows():
    word_data[value["French"]] = value["English"]

def right_word():
    """This function is called when the user selects the correct word."""
    global correct_words
    correct_words.append(word_gen)  # Add the current word to the list of correct words
    word_generator()  # Generate a new word for the next flashcard

def word_generator():
    """This function generates a random word from the list of words that need to be learned."""
    global word_gen
    global word_data

    word_to_learn = dict()  # Create a new dictionary to store words that still need to be learned
    for (key, value) in word_data.items():
        if key in correct_words:
            # Skip words that have already been answered correctly
            pass
        else:
            word_to_learn[key] = value  # Add words that haven't been answered correctly to the new dictionary

    word_data = word_to_learn  # Update the word_data to only include words that need to be learned

    # Create a pandas DataFrame from the remaining words and save them to a CSV file
    sorted_data_df = {
        "French": word_to_learn.keys(),
        "English": word_to_learn.values(),
    }

    data_to_csv = pandas.DataFrame(sorted_data_df)
    data_to_csv.to_csv("words_to_learn.csv")  # Save the words that need to be learned to a new CSV file

    canvas.itemconfig(front_image, image=image)  # Reset the front card image

    title_gen = "French"  # Set the title to "French"
    word_gen = random.choice(list(word_to_learn.keys()))  # Pick a random French word to display

    canvas.itemconfig(title, text=title_gen, fill="black")  # Set the title text to "French" in black
    canvas.itemconfig(word, text=word_gen, fill="black")  # Display the French word on the card

    # After 3 seconds, flip the card to show the English word
    window.after(3000, flip_card, True)

# Initialize the main window of the application
window = Tk()
window.title("Flashy")  # Set the window title
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)  # Set padding and background color

# Create the canvas for displaying the flashcards
canvas = Canvas(window, width=840, height=566, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")  # Load the front image of the flashcard
back_image_card = PhotoImage(file="images/card_back.png")  # Load the back image of the flashcard
front_image = canvas.create_image(430, 295, image=image)  # Place the front image on the canvas
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)  # Grid layout for the canvas

# Create the text elements for the title and word
title = canvas.create_text(428, 150, text="", font=("ariel", 40, "italic"))
word = canvas.create_text(428, 293, text="", font=("Arial", 60, "bold"))

# Create the "No" (wrong) button and add it to the window
no_image_button = PhotoImage(file="images/wrong.png")  # Load the image for the "No" button
no_button = Button(image=no_image_button, highlightthickness=0, border=0, command=word_generator)  # Create the button and bind it to word_generator
no_button.grid(column=0, row=2)  # Position the button on the grid

# Create the "Yes" (right) button and add it to the window
yes_image_button = PhotoImage(file="images/right.png")  # Load the image for the "Yes" button
yes_button = Button(image=yes_image_button, highlightthickness=0, border=0, command=right_word)  # Create the button and bind it to right_word
yes_button.grid(column=1, row=2)  # Position the button on the grid

# Generate the first word to show
word_generator()

# After 3 seconds, flip the card to show the English word
window.after(3000, flip_card, True)

# Start the main event loop for the application
window.mainloop()
