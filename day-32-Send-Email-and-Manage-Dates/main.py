# import smtplib
#
# my_email = ""
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="Subject: TFT at 6? \n\nCAN YOU SEE THIS?!!"
#     )


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
# print(type(year))
# print(type(now))
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)

# # -*- coding: utf-8 -*-
# import smtplib
# import datetime as dt
# import random
# MY_EMAIL = "reminder.imhungry@gmail.com"
# MY_PASSWORD = ""
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 6:
#     with open("quotes.txt", encoding="utf8") as quote_file:
#
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         print(quote)
#         test = quote.encode('ascii', 'ignore')
#         print(test)
#         test = test.decode("utf8")
#         print(test)
#         connection.ehlo()
#         connection.starttls()
#         connection.ehlo()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:Monday Motivation\n\n{test}")
#
# print(weekday)


from datetime import datetime
import pandas
import random
import smtplib

my_email = ""
password = ""

today = datetime.now()
print(today)
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            #connection.ehlo()
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
        print("success")
    except:
        print("failed to send mail")

#You can use Pythonanywhere to run your code in the Cloud






