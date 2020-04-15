# importing the requests library 
import requests 
import json 

#lat/lon
#Uncomment these lines for Staten Island NY
#lat = "40.643501"
#lon = "-74.076202"

#api_key
api_key=""

# api-endpoint 
URL = "http://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+api_key
print(URL) 
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
print(json.dumps(data))
