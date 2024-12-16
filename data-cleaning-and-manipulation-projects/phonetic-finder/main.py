import pandas  # Import the pandas module to handle CSV data

# Read the NATO phonetic alphabet CSV file and store it in a DataFrame
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary where each letter of the alphabet maps to its NATO phonetic code
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# The program runs in a loop, allowing the user to enter a word
is_on = True
while is_on:
    # Prompt the user to input a word
    user_text = input("Type a word: ")

    try:
        # Convert each letter in the input word to its corresponding NATO phonetic code
        result = [nato_dict[letter.upper()] for letter in user_text]
    except KeyError:
        # If a letter that is not part of the alphabet is entered, print an error message
        print("Sorry, only letters in the alphabet please.")
    else:
        # If all letters are valid, print the phonetic code representation of the word
        print(result)

        # Exit the loop after a successful input
        is_on = False
