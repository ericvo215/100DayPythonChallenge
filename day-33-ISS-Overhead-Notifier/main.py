# import requests
# from tkinter import *
#
# def get_quote():
#     response = requests.get(url="http://api.kanye.rest/")
#     response.raise_for_status()
#     print(response)
#     data = response.json()
#
#     kanye_response = data["quote"]
#     canvas.itemconfig(quote_text, text=kanye_response)
#     print(kanye_response)
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()


import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 39.9527237
MY_LONG = -75.1635262


def iss_notification():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (latitude, longitude)
    print(iss_position)
    if MY_LAT - 5 <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)

    test = data["results"]["sunrise"]
    print(test)

    time_now = datetime.now()
    print(time_now.hour)

    if time_now >= sunset or time_now <= sunrise:
        return True


MY_EMAIL = ""
MY_PASSWORD = ""

while True:
    time.sleep(60)
    if iss_notification() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up \n\nTheISS is above you in the sky."

        )

iss_notification()
print(abs(-5))
