import requests
from datetime import datetime
# change your personal information hier
GENDER = 'female'
WEIGHT_KG = 45
HEIGHT_CM = 160
AGE = 25
APP_ID="a85c5b71"
APP_KEY="13d0b21b4d36e2a2e1f8219a99670e88"

# change your sheety api post endpoint hier
sheety_post_endpoint="https://api.sheety.co/9d464d54e93643d616111bc10cf215f6/myWorkouts/workouts"

# Nutritionix API endpoint for Natural Language for Exercise
api_url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


# Plain text input for exercise (e.g., "ran 5 miles")


# Set up headers
header= {
     'x-app-id': APP_ID,
    "x-app-key": APP_KEY,
}
# Set up data payload with the exercise text
data = {
    'query': input("Tell me which excercises you did:"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Make a POST request to the Nutritionix API
response = requests.post(api_url_endpoint, headers=header, json=data)
response.raise_for_status()
data=response.json()
print(response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_post_endpoint, json=sheet_inputs)

    print(sheet_response.text)