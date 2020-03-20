import os
import report
from gtts import gTTS


temp_now = report.get_temperature_now()
temp_12 = report.get_temperature_12()
temp_18 = report.get_temperature_18()
clouds = report.get_clouds()
wind = report.get_wind_strenght()
w_dir = report.get_wind_direction()
pcat = report.get_precipitation()
ws = report.get_w_symbol()

string = ("""
    God morning! Now is {6}. Time to shine!!!
    Today is {5}.
    Air temperature now is {0} degrees. {3} and {7} wind is {4} m/s.
    {8} 
    In the daytime is going to be {1} degrees.
    Tonight can be {2} degrees.""").format(temp_now, temp_12, temp_18, clouds, wind, 
                                        report.date, report.time, w_dir, ws)

tts = gTTS(string)
tts.save("report.mp3")

os.system("omxplayer report.mp3")
