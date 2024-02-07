import datetime as dt
import pandas as pd
import random
import smtplib

MY_NUMBER = input("Enter your phone number: ")
MY_PASSWORD = input("Enter your password: ")
MY_NAME = input("Enter your name: ")

now = dt.datetime.now()
today = (now.month, now.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = str(contents).replace("[NAME]", str(birthday_person["name"]))
        connection = smtplib.SMTP_SSL("sms.ru", 465)
        connection.login(MY_NUMBER, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_NUMBER,
            to_addrs=birthday_person["number"],
            msg=f"Subject:Happy Birthday!\n\n{contents}\n\nMY_NAME"
        )
        connection.quit()
        print('Mail successfully sent.')