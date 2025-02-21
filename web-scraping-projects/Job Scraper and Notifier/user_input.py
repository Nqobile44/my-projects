import os
import json

def clear_data(file_path: str):
    with open(file=file_path, mode="w") as file:
        pass

class CollectUserInfo:
    def __init__(self):
        self.job_title = None
        self.location = None
        self.time = None
        self.email = None
        self.password = None
        self.file_path = 'data/user_data.csv'

    def collect_user_info(self):
        self.job_title = input("Enter the job title or keyword: ")
        self.location = input("Enter the workplace?\nRemote or On-Site or Hybrid: ")
        self.time = input("Enter the worktime?\nFull-Time or Part-Time: ")
        self.email = input("Enter the email used for LinkedIn: ")
        self.password = input("Enter the LinkedIn password: ")


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



        with open(file=self.file_path, mode="w") as file_empty:
            json.dump(obj=data, fp=file_empty, indent=4)


    def check_file(self, file_path: str) -> bool:
        return os.stat(file_path).st_size != 0



if __name__ == "__main__":
    collect_user_info = CollectUserInfo()
    print(collect_user_info.check_file(file_path="data/user_data.csv"))
