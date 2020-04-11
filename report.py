import datetime
import json

#Report data: now (7.30), 12.00 and 18.00
with open("weather.json", "r") as read_data:
    weather_data = json.load(read_data)
    forecast_by_time = weather_data["timeSeries"]


#More info https://opendata.smhi.se/apidocs/metfcst/parameters.html
def pick_data(string, time_now):

    """Pick data vi need from list of dictionaries forecast_by_time. Filter by time and parameter"""

    for i in range(len(forecast_by_time)):
        if forecast_by_time[i]['validTime'] == time_now:
            param_list = forecast_by_time[i]['parameters']
            for i in range(len(param_list)):
                if param_list[i]['name'] == string:
                    return param_list[i]['values'][0]

def get_temperature_now(): 
    temperature = pick_data('t', time_now)
    return round(temperature)

def get_temperature_12():
    temperature = pick_data('t', time_12)
    return round(temperature)

def get_temperature_18():
    temperature = pick_data('t', time_18)
    return round(temperature)

def get_clouds():
    clouds = ["sunny", "partly cloudy", "cloudy"]
    index = pick_data('tcc_mean', time_now)
    if index <=1:
        return clouds[0]
    elif index > 1 and index <=5:
        return clouds[1]
    elif index > 5:
        return clouds[2]

def get_precipitation():
    precipitation = ["Any precipitation", "Snow", "Snow and rain", "Rain", "Drizzle",
                    "Freezing rain", "Freezing drizzle"]
    index = pick_data('pcat', time_now)
    return precipitation[index]


def get_w_symbol():
    ws = ["Clear sky", "Nearly clear sky", "Variable cloudness", "Halfclear sky", 
    "Cloudy sky","Overcast", "Fog", "Light rain showers", "Moderate rain showers", 
    "Heavy rain showers", "Thunderstorm", "Light sleet showers", "Moderate sleet showers",
    "Heavy sleet showers", "Light snow showers", "Moderate snow showers", 
    "Heavy snow showers", "Light rain", "Moderate rain", "Heavy rain", "Thunder",
    "Light sleet", "Moderate sleet", "Heavy sleet", "Light snowfall", "Moderate snowfall",
    "Heavy snowfall"]
    index = pick_data('Wsymb2', time_now) - 1 #returns value integer, 1-27
    return ws[index]

def get_wind_direction():
    directions = ["North","Northeast","East","Southeast","South","Southwest","West","Northwest"]
    wind_d = pick_data('wd', time_now)
    if (wind_d>338 and wind_d<=359) or (wind_d>0 and wind_d<=23): return directions[0]
    elif wind_d>23 and wind_d<=78:return directions[1]
    elif wind_d>78 and wind_d<=113: return directions[2]
    elif wind_d>113 and wind_d<=157: return directions[3]
    elif wind_d>157 and wind_d<=203: return directions[4]
    elif wind_d>203 and wind_d<=248: return directions[5]
    elif wind_d>248 and wind_d<=293: return directions[6]
    elif wind_d>293 and wind_d<=338: return directions[7]


def get_wind_strenght():
    strenght = pick_data('ws', time_now)
    return str(strenght)




time_now = datetime.datetime.now().strftime("%Y-%m-%dT%H:00:00Z")
time_12 = datetime.datetime.now().strftime("%Y-%m-%dT12:00:00Z")
time_18 = datetime.datetime.now().strftime("%Y-%m-%dT18:00:00Z")
date = datetime.datetime.now().strftime("%A %B %d")
time = datetime.datetime.now().strftime("%H %M")

