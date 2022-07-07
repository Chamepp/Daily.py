import urllib3
import json

from twilio.rest import Client

# Request
http = urllib3.PoolManager()
r = http.request('GET', 'http://ipinfo.io/json')
data = json.loads(r.data.decode('utf-8'))

# Location
city=data['city']
loc=data['loc']
print(city,loc)

# Send Location
client = Client("TWILO SSID", "AUTH TOKEN")
client.messages.create(to="PHONE NO YOU WANT TO SEND SMS",
                       from_="YOUR TWILLO PHONE NUMBER",
body="Hi, Im in  " + city + "   Now and My Coordinates are  " + loc)
