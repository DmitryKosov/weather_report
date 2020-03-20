import json
import datetime

#Report data: now (7.30), 12.00 and 18.00
def get_temperature_now(): 
    temperature = forecast_by_time[0]["parameters"][11]["values"][0]
    return round(temperature)

def get_temperature_12():
    temperature = forecast_by_time[5]["parameters"][11]["values"][0]
    return round(temperature)

def get_temperature_18():
    temperature = forecast_by_time[11]["parameters"][1]["values"][0]
    return round(temperature)

def get_clouds():
    clouds = ["sunny", "partly cloudy", "cloudy"]
    index = forecast_by_time[0]["parameters"][6]["values"][0]
    if index <=1:
        return clouds[0]
    elif index > 1 and index <=5:
        return clouds[1]
    elif index > 5:
        return clouds[2]

def get_precipitation():
    precipitation = ["Any precipitation", "Snow", "Snow and rain", "Rain", "Drizzle",
                    "Freezing rain", "Freezing drizzle"]
    index = forecast_by_time[0]["parameters"][1]["values"][0]
    return precipitation[index]


def get_w_symbol():
    ws = ["Clear sky", "Nearly clear sky", "Variable cloudness", "Halfclear sky", 
    "Cloudy sky","Overcast", "Fog", "Light rain showers", "Moderate rain showers", 
    "Heavy rain showers", "Thunderstorm", "Light sleet showers", "Moderate sleet showers",
    "Heavy sleet showers", "Light snow showers", "Moderate snow showers", 
    "Heavy snow showers", "Light rain", "Moderate rain", "Heavy rain", "Thunder",
    "Light sleet", "Moderate sleet", "Heavy sleet", "Light snowfall", "Moderate snowfall",
    "Heavy snowfall"]
    index = forecast_by_time[0]["parameters"][18]["values"][0] - 1 #returns value integer, 1-27
    return ws[index]

def get_wind_direction():
    directions = ["North","Northeast","East","Southeast","South","Southwest","West","Northwest"]
    wind_d = forecast_by_time[0]["parameters"][13]["values"][0]
    if (wind_d>338 and wind_d<=359) or (wind_d>0 and wind_d<=23): return directions[0]
    elif wind_d>23 and wind_d<=78:return directions[1]
    elif wind_d>78 and wind_d<=113: return directions[2]
    elif wind_d>113 and wind_d<=157: return directions[3]
    elif wind_d>157 and wind_d<=203: return directions[4]
    elif wind_d>203 and wind_d<=248: return directions[5]
    elif wind_d>248 and wind_d<=293: return directions[6]
    elif wind_d>293 and wind_d<=338: return directions[7]


def get_wind_strenght():
    strenght = forecast_by_time[0]["parameters"][14]["values"][0]
    return str(strenght)

with open("weather.json", "r") as read_data:
    weather_data = json.load(read_data)
    forecast_by_time = weather_data["timeSeries"]

timeStample = datetime.datetime.now().strftime("%Y-%m-%dT%H:00:00Z")
date = datetime.datetime.now().strftime("%A %B %d")
time = datetime.datetime.now().strftime("%H %M")
