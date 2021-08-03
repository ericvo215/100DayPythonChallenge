import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
print(os.environ.get("OWM_API_KEY"))
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("T_ACCOUNT_SID")
auth_token = os.environ.get("T_AUTH_TOKEN")

weather_params = {
    "lat": 39.7447,
    "lon": -75.5484,
    "appid": api_key
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(response.status_code)
print(response.json())
weather_slice = weather_data["hourly"][:12]

will_rain = False

#print(weather_data["hourly"[0]]["weather"][0]["id"])
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today",
        from_=os.environ.get("FROMNUMBER"),
        to=os.environ.get("TONUMBER")
    )
    print("hi")

