import urllib.request, urllib.parse, urllib.error


latitude = "59.1658"
longitude = "18.1979"

#Raspbian has Python 3.5.3, hasn't f-string 
string = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{0}/lat/{1}/data.json".format(longitude, latitude)
weather = urllib.request.urlopen(string)

size = 0
fhand = open("weather.json", "wb")
while True:
    info = weather.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
fhand.close()