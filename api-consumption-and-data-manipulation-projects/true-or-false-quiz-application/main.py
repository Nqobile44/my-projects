# Import necessary modules and classes
from question_model import Question  # The Question class to create question objects
from data import question_data  # A dictionary of question data
from quiz_brain import QuizBrain  # The QuizBrain class that controls the quiz flow
from ui import GuiQuiz  # The GuiQuiz class for the graphical user interface

# Create an empty list to hold all the question objects
question_bank = []

# Loop through the raw question data and convert each item to a Question object
for question in question_data:
    question_text = question["question"]  # Get the question text from the dictionary
    question_answer = question["correct_answer"]  # Get the correct answer from the dictionary
    new_question = Question(question_text, question_answer)  # Create a new Question object
    question_bank.append(new_question)  # Add the question object to the question_bank list

# Create a new QuizBrain object using the question_bank
quiz = QuizBrain(question_bank)

# Initialize the graphical user interface for the quiz
gui_quiz = GuiQuiz(quiz)

# After the quiz is completed, display the final score
print("You've completed the quiz")  # Print a message that the quiz is over
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  # Display the user's score

