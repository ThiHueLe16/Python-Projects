import datetime
import requests
from tkinter import *
# --------------------------------CHANGE YOUR PERSONAL INFORMATION BELOW---------------------------------------
# read README.md for usage tutoral
MY_LAT = "lattitude of your current place (type int) "
MY_LONG = "long titude of your current place in int (type int)"
MY_CITY = "your city name "
COUNTRY_CODE = 'your country code, for exp.: US, DE, ...(type string)'
weather_api_key = 'your weather api key(type string)'

# --------------------------------------------------------------------------------------------------------------

weather_api_endpoint = 'http://api.openweathermap.org/data/2.5/weather'
weather_forecast_api_endpoint="https://api.openweathermap.org/data/2.5/forecast"
BACKGROUND_COLOR = "#FFD1E3"
FONT_COLOR = "#33186B"
UNDERLINE = "----------------------------------------------------------------------------------------------------"


def getCurrentWeekDays():
    today = datetime.date.today()
    curent_week_days_Date = [today + datetime.timedelta(days=i) for i in range(5)]
    print(curent_week_days_Date)
    return curent_week_days_Date


def get_Sunrise_Sunset_Time(date):
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "date": date,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
    print(f"On {date}, at Munich location ({MY_LAT}, {MY_LONG}):")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")
    return f"Sunrise: {sunrise}       Sunset: {sunset}"


def getTemperature():
    parameters = {
        'q': f'{MY_CITY},{COUNTRY_CODE}',
        'appid': weather_api_key,
        'units': 'metric'  # Use 'metric' for Celsius or 'imperial' for Fahrenheit
    }
    response = requests.get(url=weather_api_endpoint, params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    # cur_temperature = data['main']['temp']
    print(f"The current temperature in {MY_CITY} is {data['main']['temp']}°C")
    return data

def getForecast5days():
    forecast_params={
        'lat': MY_LAT,
        'lon': MY_LONG,
        # 'cnt': 7,
        'appid': weather_api_key,
        'units': 'metric'
    }
    response = requests.get(url=weather_forecast_api_endpoint, params=forecast_params)
    response.raise_for_status()
    data=response.json()
    return data

"-------------------------------------CREATE GUI--------------------------------------------"
temps_Today_Data = getTemperature()

window = Tk()
window.title("Sunrise_sunset Forecast")
window.config(width=600, height=400, bg=BACKGROUND_COLOR, padx=50, pady=50)

cityLabel = Label(text=MY_CITY, fg="#392467", bg=BACKGROUND_COLOR, font=("Times New Roman", 60, "bold"))
cityLabel.grid(row=0, column=0)
curTempLabel = Label(text=f"{temps_Today_Data['main']['temp']} °C ", fg="#392467", bg=BACKGROUND_COLOR,
                     font=("Arial", 30))
curTempLabel.grid(row=1, column=0)
description = Label(text=f"{temps_Today_Data['weather'][0]['description']}", fg="#392467", bg=BACKGROUND_COLOR,
                    font=("Arial", 15))
description.grid(row=2, column=0)
min_max_Temp = Label(text=f"L:{temps_Today_Data['main']['temp_min']} °C   H:{temps_Today_Data['main']['temp_max']} °C",
                     fg="#392467", bg=BACKGROUND_COLOR, font=("Arial", 15))
min_max_Temp.grid(row=3, column=0)
canvas = Canvas(window, width=400, height=650, bg="#C499F3", highlightthickness=0)
text1 = canvas.create_text(100, 40, text="5 DAYS FORECAST", font=("Arial", 18), fill=FONT_COLOR)
text2 = canvas.create_text(100, 80, text=UNDERLINE, font=("Arial", 18), fill=FONT_COLOR)
canvas.grid(row=4, column=0)

currentWeekDates = getCurrentWeekDays()
weekday = []
for i in range(5):
    curDate = currentWeekDates[i].strftime("%d-%m-%Y")
    date_parameter = currentWeekDates[i].strftime("%Y-%m-%d")
    forecast5Days=getForecast5days()
    temps= f"Temp:{forecast5Days['list'][8*i]['main']['temp']}°C"
    curDateDescription=f"{forecast5Days['list'][8*i]['weather'][0]['description']} "
    canvas.create_text(90, 100 + i * 100, text=curDate, font=("Arial", 15, "bold"), fill=FONT_COLOR)
    canvas.create_text(100, 100 + i * 100 + 20, text=temps, font=("Arial", 15),fill=FONT_COLOR)
    canvas.create_text(102, 100 + i * 100 + 40, text=curDateDescription, font=("Arial", 15), fill=FONT_COLOR)
    canvas.create_text(180, 100 + i * 100 + 60, text=get_Sunrise_Sunset_Time(date_parameter), font=("Arial", 15),fill=FONT_COLOR)
    canvas.create_text(100, 100 + i * 100 + 80, text=UNDERLINE, font=("Arial", 18), fill=FONT_COLOR)
getForecast5days()
window.mainloop()
