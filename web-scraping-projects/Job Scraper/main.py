from user_input import CollectUserInfo  # Importing class for user input handling
from user_input import clear_data   # Function to clear saved user data
from internet import GetToLinkedIn  # Class to handle LinkedIn scraping
import json # To handle JSON data

# Instantiate the CollectUserInfo class for collecting user data
collect_info = CollectUserInfo()

data = None
def clean_avail_job():
    global data
    """Cleans and prepares available jobs for printing to the console."""
    with open(file="data/job_data.csv", mode="r") as file:
        data = json.load(fp=file)

    message = ""
    if not data:
        return False

    # Format the job information into a message string
    for job in data:
        message += f"Job Title: {job["job_title"]}\n\n"
        message += f"Company Name: {job["company_name"]}\n\n"
        message += f"Posted Time: {job["posted_time"]}\n\n"
        message += f"Job Link: {job["job_link"]}\n\n"
        message += f"Job Address: {job["job_address"]}\n\n"
        message += f"Job Summary: {job["job_description"]}\n\n\n\n"

    return message


def get_jobs_to_file():
    """Logs into LinkedIn, collects job postings, and saves them to a CSV file."""
    get_to_linkedin = GetToLinkedIn()
    get_to_linkedin.login()
    get_to_linkedin.get_jobs()
    get_to_linkedin.quit()

def func_call():
    """Calls user info collection based on a condition."""
    global user_info_check
    try:
        user_info_check.lower()
    except (AttributeError, NameError):
        pass
    else:
        if user_info_check.lower():
            collect_info.collect_user_info()
        else:
            ...

# Check if user data already exists
if collect_info.check_file(file_path="data/user_data.csv"):
    user_choice = input("1. Own Data\n2. Saved Data\nSelect data you use: ")
    if user_choice == "1":
        collect_info.collect_user_info()

    func_call()

else:
    collect_info.collect_user_info()
    func_call()

# Ask user if they want to keep their personal information
user_info_check = input("Do you keep the personal information?\nIf you keep press 'Enter', if not type N:\n")

# Run the LinkedIn job collection process
get_jobs_to_file()
print(clean_avail_job())

# Clear user data if the user chooses not to keep it
if user_info_check:
    clear_data(file_path="data/user_data.csv")
