import os
import json

# Function to clear the contents of a file by opening it in write mode
def clear_data(file_path: str):
    with open(file=file_path, mode="w") as file:
        pass    # Opening in write mode with no content will empty the file

# Class to collect and store user information in a JSON format
class CollectUserInfo:
    def __init__(self):
        # Initializing instance variables for job and personal information
        self.job_title = None
        self.location = None
        self.time = None
        self.email = None
        self.password = None
        self.file_path = 'data/user_data.csv'   # File path where user data will be saved

    # Method to collect user information and save it to a file in JSON format
    def collect_user_info(self):
        # Collecting user input for job-related data
        self.job_title = input("Enter the job title or keyword: ")
        self.location = input("Enter the workplace?\nRemote or On-Site or Hybrid: ")
        self.time = input("Enter the worktime?\nFull-Time or Part-Time: ")

        # Collecting user input for personal details
        self.email = input("Enter the email used for LinkedIn: ")
        self.password = input("Enter the LinkedIn password: ")

        # Structuring the collected data into a dictionary
        data = {
            "job_data": {
                "job_title": self.job_title,
                "workplace": self.location,
                "time": self.time,
            },
            "personal": {
                "email": self.email,
                "password": self.password,
            }
        }

        # Writing the structured data to a file in JSON format
        with open(file=self.file_path, mode="w") as file_empty:
            json.dump(obj=data, fp=file_empty, indent=4)

    # Method to check if the file at the given path is empty
    def check_file(self, file_path: str) -> bool:
        # Using os.stat to check the file size and determine if it's empty
        return os.stat(file_path).st_size != 0  # Return True if the file is not empty, False otherwise
