from user_input import CollectUserInfo
from user_input import clear_data
from internet import GetToLinkedIn
import json

collect_info = CollectUserInfo()

data = None
def clean_avail_job():
    global data
    """This cleans and prepares available jobs for email, and send the data."""
    with open(file="data/job_data.csv", mode="r") as file:
        data = json.load(fp=file)

    message = ""
    if not data:
        return False
    for job in data:
        message += f"Job Title: {job["job_title"]}\n\n"
        message += f"Company Name: {job["company_name"]}\n\n"
        message += f"Posted Time: {job["posted_time"]}\n\n"
        message += f"Job Link: {job["job_link"]}\n\n"
        message += f"Job Address: {job["job_address"]}\n\n"
        message += f"Job Summary: {job["job_description"]}\n\n\n\n"

    return message


def get_jobs_to_file():
    """This gets all the jobs from the LinkedIn website to csv file."""
    get_to_linkedin = GetToLinkedIn()
    get_to_linkedin.login()
    get_to_linkedin.get_jobs()
    get_to_linkedin.quit()

def func_call():
    global user_info_check
    try:
        user_info_check.lower()
    except:
        pass
    else:
        if user_info_check.lower():
            collect_info.collect_user_info()
        else:
            ...

# input from the user, save data to csv file.
if collect_info.check_file(file_path="data/user_data.csv"):
    user_choice = input("1. Own Data\n2. Saved Data\nSelect data you use: ")
    if user_choice == "1":
        collect_info.collect_user_info()

    func_call()

else:
    collect_info.collect_user_info()
    func_call()

user_info_check = input("Do you keep the personal information?\nIf you keep press 'Enter', if not type N:\n")

get_jobs_to_file()
print(clean_avail_job())

if user_info_check:
    clear_data(file_path="data/user_data.csv")
