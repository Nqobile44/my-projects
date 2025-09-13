from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
import time


class SendDetails:
    def __init__(self, product_name, current_price, url):
        self.name = product_name
        self.price = current_price
        self.url = url
        self.message = f'Price alert: {self.name} is now R{self.price}. Grab it before it goes back up: {self.url}'

    def send_email(self):
        sender = 'serciiemmanuel@gmail.com'
        receiver = 'dlamininqobile80@gmail.com'
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'Price alert'
        message.attach(MIMEText(self.message, "plain", "utf-8"))

        print(self.message)

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=sender, password="zlcmbwrgimbloana")
            connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message.as_string())


        

class PriceTracker:
    def __init__(self, url, price):
        self.url = url
        self.price = price

        contents = requests.get(url=self.url)
        self.soup = BeautifulSoup(contents.text, 'html.parser')

    def price_checker(self):
        real_price = self.soup.find(name='span', class_='a-offscreen').text
        real_price = real_price.replace("R", "").replace("\xa0", "").replace(',00', '').strip()
        if int(real_price) <= int(self.price):
            return real_price
        else:
            return False

with open('auto_price_tracker/data.json') as file:
    data = json.load(file)

while True:
    for index in range(len(data)):
        name = data[index]['name']
        url = data[index]['url']
        price = data[index]['price']

        price_tracker = PriceTracker(url=url, price=price)
        result = price_tracker.price_checker()
        if result:
            send_details = SendDetails(name, price, url)
            send_details.send_email()

    time.sleep(600000)




