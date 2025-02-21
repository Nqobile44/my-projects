from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import datetime
import os

def data_extract():
    """ This get user email and password from csv file."""
    with open(file="data/user_data.csv", mode="r") as file:
        data = json.load(fp=file)

    return data

def clear_job_data() -> bool:
    """It cleans/ erases job_data.csv file."""
    with open(file="data/job_data.csv", mode="w") as _:
        pass

    return True


def date_track() -> bool:
    """It tracks the date making sure if date is a new day if true then it clean job_data.csv file else it keeps the data in the file."""
    date = str(datetime.datetime.now().date())

    with open(file="data/date_trackerk.txt", mode="r") as file:
        old_date = file.read()

    if date == old_date:
        return True

    else:
        with open(file="data/date_trackerk.txt", mode="w") as file:
            file.write(date)
        return clear_job_data()


class GetToLinkedIn:
    def __init__(self):
        self.data = data_extract()
        self.email = self.data["personal"]["email"]
        self.password = self.data["personal"]["password"]

        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option(name="detach", value=True)

        self.driver = webdriver.Edge(options=edge_options)


    def login(self):
        """This search the jobs based on user input."""
        self.driver.get(url="https://linkedin.com")

        email_login_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="#main-content > section.section.min-h-68.flex-nowrap.pt-6.babybear\:flex-col.babybear\:min-h-0.babybear\:px-mobile-container-padding.babybear\:pt-3 > div > div > a")
        email_login_btn.click()

        email_input = self.driver.find_element(by=By.CSS_SELECTOR, value="#username")
        email_input.send_keys(self.email)

        password_input =self.driver.find_element(by=By.CSS_SELECTOR, value="#password")
        password_input.send_keys(self.password)

        submit_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="#organic-div > form > div.login__form_action_container > button")
        submit_btn.click()

    def get_jobs_to_file(self) -> bool:
        """This takes the information of all the jobs that meet the user requirement and put them in to csv file."""
        job_title = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/h1/a")


        company_name = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/a").text
        try:
            posted_time = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/span[3]/span").text
        except:
            try:
                posted_time = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/span[3]/span[2]").text
            except:
                posted_time = "None"
        try:
            job_address = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/span[1]").text

        except:
            job_address = "None"


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


        job_link = job_title.get_attribute("href")

        date_track()


        file_path = 'data/job_data.csv'
        if os.stat(file_path).st_size == 0:
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
        """This check if the work-time corresponds with the user work-time."""
        time.sleep(1)
        worktime_path = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/button/div[2]/span/span[1]"

        if self.data["job_data"]["time"].lower() == "full-time":
            try:
                worktime_element = self.driver.find_element(by=By.XPATH, value=worktime_path)

            except:
                tick = False

            else:
                worktime_text = worktime_element.text.strip()
                if worktime_text != "Full-time":
                    tick = False


        elif self.data["job_data"]["time"].lower() == "part-time":

            try:
                worktime_element = self.driver.find_element(by=By.XPATH, value=worktime_path)

            except:
                tick = False

            else:
                worktime_text = worktime_element.text.strip()
                if worktime_text != "Part-time":
                    tick = False

        if tick:
            return self.get_jobs_to_file()
        else:
            return False

    def check_workplace(self, tick) -> bool:
        """This check if the work-place corresponds with the user work-place."""

        workplace_path = "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > button > div:nth-child(1) > span > span:nth-child(1)"

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
                    if workplace_text != "Remote":
                        tick = False


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

        if tick:
            return self.check_worktime(tick)
        else:
            return False


    def get_jobs(self):
        """This takes all the jobs that meet the requirements and that is not in csv file""" #this help to not send the same jobs to the user.
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
        try:
            job_list = self.driver.find_elements(by=By.XPATH, value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li")
        except:
            time.sleep(10)
            job_list = self.driver.find_elements(by=By.XPATH,
                                                 value="/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li")

        for index in range(len(job_list)):
            tick = True
            if index != 0:
                job_list[index].click()

                if self.check_workplace(tick):
                    print(True)

                else:
                    pass

                time.sleep(1)


    def quit(self):
        """This quit the whole program"""
        self.driver.quit()

if __name__ == "__main__":
    get_to_linkedin = GetToLinkedIn()
    get_to_linkedin.login()
    get_to_linkedin.get_jobs()
    get_to_linkedin.quit()
