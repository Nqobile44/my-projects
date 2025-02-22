from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import datetime
import os

# Function to extract user credentials from a CSV file
def data_extract():
    """Get user email and password from a CSV file."""
    with open(file="data/user_data.csv", mode="r") as file:
        data = json.load(fp=file)

    return data

# Function to clear job data
def clear_job_data() -> bool:
    """Erase job_data.csv file to clear stored job data."""
    with open(file="data/job_data.csv", mode="w") as _:
        pass

    return True

# Function to track date changes and clear data for a new day
def date_track() -> bool:
    """Clear job data if it's a new day."""
    date = str(datetime.datetime.now().date())

    with open(file="data/date_trackerk.txt", mode="r") as file:
        old_date = file.read()

    if date == old_date:
        return True # Same day, keep the data

    else:
        with open(file="data/date_trackerk.txt", mode="w") as file:
            file.write(date)
        return clear_job_data() # New day, clear the data

# Class to handle LinkedIn automation
class GetToLinkedIn:
    def __init__(self):
        # Load user credentials from the extracted data
        self.data = data_extract()
        self.email = self.data["personal"]["email"]
        self.password = self.data["personal"]["password"]

        # Setup Edge WebDriver options to keep the browser open after script ends
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Edge(options=edge_options)

    def login(self):
        """Log in to LinkedIn using user credentials."""
        self.driver.get(url="https://linkedin.com")

        # Click login button and input credentials
        email_login_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="#main-content > section.section.min-h-68.flex-nowrap.pt-6.babybear\:flex-col.babybear\:min-h-0.babybear\:px-mobile-container-padding.babybear\:pt-3 > div > div > a")
        email_login_btn.click()

        email_input = self.driver.find_element(by=By.CSS_SELECTOR, value="#username")
        email_input.send_keys(self.email)

        password_input =self.driver.find_element(by=By.CSS_SELECTOR, value="#password")
        password_input.send_keys(self.password)

        submit_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="#organic-div > form > div.login__form_action_container > button")
        submit_btn.click()

    def get_jobs_to_file(self) -> bool:
        """Extract job info from LinkedIn and save it to a CSV file."""
        # Extract job details (title, company, location, etc.)
        job_title = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/h1/a")


        company_name = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/a").text

        # Try to get posting time; set to 'None' if not found
        try:
            posted_time = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/span[3]/span").text
        except:
            try:
                posted_time = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/span[3]/span[2]").text
            except:
                posted_time = "None"

        # Try to get job address; set to 'None' if not found
        try:
            job_address = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/span[1]").text

        except:
            job_address = "None"

        # Try to get job description; handle missing elements gracefully
        try:
            job_description1 = self.driver.find_element(by=By.XPATH, value="//html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[4]/article/div/div[1]/div/p/span[3]/p").text

        except:
            job_description = "None"

        else:
            try:
                job_description2 = self.driver.find_element(by=By.XPATH,
                                                            value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[4]/article/div/div[1]/div/p/span[5]/p").text
            except:
                job_description = "None"
            else:
                job_description = f"{job_description1}\n{job_description2}"

        # Extract job link from the job title element
        job_link = job_title.get_attribute("href")

        # Check if it's a new day and clear job data if necessary
        date_track()

        # Save or append job data to CSV
        file_path = 'data/job_data.csv'
        if os.stat(file_path).st_size == 0:
            # File is empty; write new data
            job_data = [
                {
                    "job_title": job_title.text,
                    "company_name": company_name,
                    "posted_time": posted_time,
                    "job_link": job_link,
                    "job_address": job_address,
                    "job_description": job_description
                }
            ]
            with open(file="data/job_data.csv", mode="w") as file:
                json.dump(obj=job_data, fp=file, indent=4)

        else:
            # Load existing data and append new job if not duplicated
            with open(file="data/job_data.csv", mode="r") as file:
                data = json.load(file)
                job_data = {
                        "job_title": job_title.text,
                        "company_name": company_name,
                        "posted_time": posted_time,
                        "job_link": job_link,
                        "job_address": job_address,
                        "job_description": job_description
                    }

            # Avoid duplicates based on title, company, and post time
            for job in data:
                if job["job_title"] == job_data["job_title"]\
                        and job["company_name"] == job_data["company_name"]\
                        and job["posted_time"] == job_data["posted_time"]:
                    return False

            data.append(job_data)

            with open("data/job_data.csv", "w") as file1:
                json.dump(obj=data, fp=file1, indent=4)

        return True


    def check_worktime(self, tick) -> bool:
        """This checks if the job's work-time matches the user's preference (Full-time or Part-time)."""
        time.sleep(1)   # Wait for the element to load
        worktime_path = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/button/div[2]/span/span[1]"

        # Check for Full-time jobs
        if self.data["job_data"]["time"].lower() == "full-time":
            try:
                worktime_element = self.driver.find_element(by=By.XPATH, value=worktime_path)

            except:
                tick = False

            else:
                worktime_text = worktime_element.text.strip()
                if worktime_text != "Full-time":
                    tick = False

        # Check for Part-time jobs
        elif self.data["job_data"]["time"].lower() == "part-time":

            try:
                worktime_element = self.driver.find_element(by=By.XPATH, value=worktime_path)

            except:
                tick = False

            else:
                worktime_text = worktime_element.text.strip()
                if worktime_text != "Part-time":
                    tick = False

        # Return the result based on the tick status
        if tick:
            return self.get_jobs_to_file()  # Proceed if the work-time matches
        else:
            return False    # Otherwise, skip

    def check_workplace(self, tick) -> bool:
        """This checks if the job's workplace setting matches the user's preference (Remote, Hybrid, or On-site)."""

        workplace_path = "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > button > div:nth-child(1) > span > span:nth-child(1)"

        # Check for Remote jobs
        if self.data["job_data"]["workplace"].lower() == "remote":
            try:
                workplace_element = self.driver.find_element(by=By.CSS_SELECTOR, value=workplace_path)

            except:
                tick = False

            else:
                try:
                    workplace_text = workplace_element.text.strip()
                except:
                    tick = False
                else:
                    if workplace_text != "Remote":  # Compare workplace setting
                        tick = False

        # Check for Hybrid jobs
        elif self.data["job_data"]["workplace"].lower() == "hybrid":

            try:
                workplace_element = self.driver.find_element(by=By.XPATH, value=workplace_path)

            except:
                tick = False

            else:
                try:
                    workplace_text = workplace_element.text.strip()
                except:
                    tick = False

                else:
                    if workplace_text != "Hybrid":
                        tick = False

        # Default to On-site if not Remote or Hybrid
        else:

            try:
                workplace_element = self.driver.find_element(by=By.XPATH, value=workplace_path)

            except:
                tick = False

            else:
                try:
                    workplace_text = workplace_element.text.strip()
                except:
                    tick = False

                else:
                    if workplace_text != "On-site":
                        tick = False

        # If workplace matches, check work-time next
        if tick:
            return self.check_worktime(tick)
        else:
            return False


    def get_jobs(self):
        """Finds jobs that meet user criteria and are not already saved in the CSV file."""
        try:
            search_input = self.driver.find_element(by=By.CSS_SELECTOR, value="#global-nav-typeahead > input")
        except:
            time.sleep(30)
            search_input = self.driver.find_element(by=By.CSS_SELECTOR, value="#global-nav-typeahead > input")

        search_input.send_keys(self.data["job_data"]["job_title"], Keys.ENTER)


        try:
            job_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
        except:
            time.sleep(5)
            job_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')

        job_btn.click()
        time.sleep(5)

        # Get the list of available jobs
        try:
            job_list = self.driver.find_elements(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li")
        except:
            time.sleep(10)
            job_list = self.driver.find_elements(by=By.XPATH,
                                                 value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li")

        # Loop through each job and validate
        for index in range(len(job_list)):
            tick = True # Reset tick for each job
            if index != 0:  # Skip the first job (possibly a header or invalid entry)
                job_list[index].click() # Click the job listing

                if self.check_workplace(tick):  # Check workplace criteria first
                    print(True) # Job meets all criteria

                else:
                    pass    # Skip if criteria not met

                time.sleep(1)   # Small delay between checking jobs


    def quit(self):
        """Close the browser and quit the program."""
        self.driver.quit()
