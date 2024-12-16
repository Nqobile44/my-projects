import html

class QuizBrain:
    def __init__(self, q_list):
        # Initializes the QuizBrain object with the provided list of questions
        self.question_number = 0  # The number of questions asked so far
        self.score = 0  # The user's score
        self.question_list = q_list  # The list of questions
        self.current_question = None  # Placeholder for the current question object

    def still_has_questions(self):
        # Returns True if there are still questions left to ask, otherwise False
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Retrieves the next question from the question list and increments the question number
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Unescapes any HTML entities in the question text (e.g., &quot; becomes ")
        q_text = html.unescape(self.current_question.text)
        # Returns a formatted string with the current question number and text
        return f"Q.{self.question_number}: {q_text}"
        # The following code would be used to get user input and check the answer:
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        # Checks if the user's answer is correct
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment score if the answer is correct
            return True
        else:
            return False

