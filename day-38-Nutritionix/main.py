import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 200
AGE = 25

NUTRITIONIX_ID = os.environ["NUTRITIONIX_ID"]
NUTRITIONIX_KEY = os.environ["NUTRITIONIX_KEY"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["sheet_endpoint"]

exercise_text = input("Tell me what exercise you did today: ")

header_params = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=user_params, headers=header_params)
result = response.json()
print(response.text)
#print(response.json()["exercises"])

today = datetime.now()
print(today)

this_date = (today.strftime("%m/%d/%Y"))
print(today.strftime("%m/%d/%Y"))

this_time = (today.strftime("%H:%M"))
print(today.strftime("%H:%M"))

exercise = response.json()["exercises"][0]["user_input"]
print(f"Exercise: {exercise}")

duration = (response.json()["exercises"][0]["duration_min"])
print(f"Duration: {duration}")

calories = (response.json()["exercises"][0]["nf_calories"])
print(f"Calories: {calories}")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": this_date,
            "time": this_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    # #Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["USERNAME"],
    #         os.environ["PASSWORD"],
    #     )
    # )

    # #Bearer Token
    # bearer_headers = {
    # "Authorization": f"Bearer {os.environ['TOKEN']}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    print(sheet_response.text)