# Import the requests library to make HTTP requests
import requests

# Make a GET request to the Open Trivia Database API to fetch 10 boolean-type questions
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")

# Parse the JSON response and extract the "results" key, which contains the list of questions
question_data = response.json()["results"]
