from tkinter import *  # Import all necessary components from Tkinter for creating the GUI
from quiz_brain import QuizBrain  # Import the QuizBrain class that handles the quiz logic

THEME_COLOR = "#375362"  # Define a color for the theme of the GUI

class GuiQuiz:
    # The constructor method initializes the GUI and sets up the layout
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # Initialize the quiz logic
        self.window = Tk()  # Create the main window for the quiz
        self.window.title("Quizzler")  # Set the title of the window
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)  # Set the background color and padding for the window

        # Create a Label widget to display the score
        self.score = Label(text=f"score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)  # Position the score label using grid layout

        # Create a Canvas widget to display the questions
        self.canvas = Canvas(self.window, width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, text="Question here", width=290, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)  # Position the canvas

        # Load and set the image for the "False" button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, border=0, command=self.false_button_check)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)  # Position the "False" button

        # Load and set the image for the "True" button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, border=0, command=self.true_button_check)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)  # Position the "True" button

        # Get the next question to display on the GUI
        self.get_next_question()

        self.window.mainloop()  # Start the Tkinter event loop to make the window interactive

    # This method updates the canvas with the next question if available
    def get_next_question(self):
        self.canvas.config(bg="white")  # Reset the background color to white for the next question
        if self.quiz.still_has_questions():  # Check if there are still more questions
            q_text = self.quiz.next_question()  # Get the next question text from the quiz logic
            self.score.config(text=f"Score {self.quiz.score}")  # Update the score label with the current score
            self.canvas.itemconfig(self.q_text, text=q_text)  # Update the question text on the canvas
        else:
            # If there are no more questions, display a message indicating the end of the quiz
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the questions.")
            self.true_button.config(state="disabled")  # Disable the "True" button
            self.false_button.config(state="disabled")  # Disable the "False" button

    # This method handles the user's click on the "True" button and gives feedback
    def true_button_check(self):
        self.give_feedback(self.quiz.check_answer("True"))  # Pass "True" answer to quiz logic and provide feedback

    # This method handles the user's click on the "False" button and gives feedback
    def false_button_check(self):
        self.give_feedback(self.quiz.check_answer("False"))  # Pass "False" answer to quiz logic and provide feedback

    # This method provides feedback by changing the canvas background color based on the correctness of the answer
    def give_feedback(self, is_right: bool):
        if is_right:  # If the answer is correct
            self.canvas.config(bg="green")  # Set the background color to green
        else:  # If the answer is incorrect
            self.canvas.config(bg="red")  # Set the background color to red

        # After 1 second, load the next question
        self.window.after(1000, self.get_next_question)  # Delay the next question update by 1 second

