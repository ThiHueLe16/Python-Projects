import requests
from datetime import datetime
MY_LAT = 48.135124
MY_LONG = 11.581981

# change formatted to 0 to set hour in 24 hours format
parameter = {"lat": MY_LAT,
             "lng": MY_LONG,
             "formatted":0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()

sunrise_time= data["results"]["sunrise"].split("T")[1].split("+")[0]
print(f"sunrise_time:{sunrise_time}")
time_now=datetime.now().time()
print(f"time_now: {time_now}")