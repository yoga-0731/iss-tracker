import requests
from datetime import datetime
import smtplib
import time

LATITUDE = 11.001812
LONGITUDE = 76.962843

USER = "python.test.googol@gmail.com"
PASSWORD = "test1234"


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()  # Raises exception when there is no successful response

    data = iss_response.json()["iss_position"]
    iss_latitude = float(data['latitude'])
    iss_longitude = float(data['longitude'])

    if LATITUDE-5 <= iss_latitude <= LATITUDE+5 and LONGITUDE-5 <= iss_longitude <= LONGITUDE+5:
        return True


def is_night():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0  # 24-hour format
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    now = datetime.now()
    if now.hour <= sunrise_hour or now.hour >= sunset_hour:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(
                from_addr=USER,
                to_addrs=USER,
                msg=f"Subject: ISS Overhead Notification!\n\nLook Up!👆ISS is above you in the night sky!!"
            )

