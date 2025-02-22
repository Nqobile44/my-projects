import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMessage: # Right here there is an issue the data im trying to send via email it excepted based on the format so im using this method, I got from chatgbt, in this case i need to get the recipient email from the user_data file and other things, comform new method with chatgbt
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

        with open(file="data/user_data.csv", mode="r") as file:
            data = json.load(fp=file)
        self.sender_email = "serciiemmanuel@gmail.com"
        self.receiver_email = data["personal"]["email"]

        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = self.subject
        self.message.attach(MIMEText(self.body, "plain", "utf-8"))

    def send_sms(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password="zlcmbwrgimbloana")
            connection.sendmail(from_addr=self.sender_email, to_addrs=self.receiver_email,
                                msg=self.message.as_string())

        print("Email Sent Successful.")


if __name__ == "__main__":
    send_message = SendMessage("hellow", "It's Me")
    send_message.send_sms()
