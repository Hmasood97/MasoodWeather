#Tweepy is where a lot of the stuff goes for 
import tweepy
import time
import urllib
import sys 
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
print("Twitter bot")

#Twitter developer stuff to tell 
CONSUMER_KEY= 'YOUR KEY'
CONSUMER_SECRET = 'YOUR SECRET'
ACCESS_KEY  = ‘YOUR ACCESS KEY'
ACCESS_SECRET = 'YOUR ACCESS_SECRET'

#forecast.io api stuff 

LATITUDE = your latitude'
LONGITUDE = your longitude'
FORECAST_IO_APIKEY = 'YOUR API KEY'

#Tweepy authentication stuff
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

#Taking in the forcecast.io
url = "https://api.forecast.io/forecast/" + FORECAST_IO_APIKEY + "/" + LATITUDE + "," + LONGITUDE
response = urllib.request.urlopen(url);
data = json.loads(response.read())

#tweetSomething you use api.update_status()

temperature = str(int(round(data['currently']['temperature'])))
degree_sign = u'\N{DEGREE SIGN}'
summary = data['daily']['summary']
today = data['hourly']['summary']
wind = int(data["currently"]["windSpeed"]),
#tells a category of the weather such as cloudy
icon = data['currently']['icon']
emoji = " "

##checking the weather and putting the emoji in
if "clear-day" in icon:
    emoji = "\U00002600"
elif "clear-night" in icon:
    emoji = "\U0001F319"
elif "cloudy" in icon:
    emoji = "\U00002601"
elif "rain" in icon:
    emoji = "\U00002614"
elif "partly-cloudy-day" in icon:
    emoji = "\U000026C5"
elif "partly-cloudy-night" in icon:
    emoji = "\U00002601"
elif "thunderstorm" in icon:
    emoji = "\U000026C8"
elif "snow" in icon:
    emoji = "\U00002744"
elif "tornado"  in icon:
    emoji = "\U0001F32A"
elif "wind" in icon:
    emoji = "\U0001F4A8"
elif "fog" in icon:
    emoji = "\U0001F32B"
elif "sleet" or "hail" in icon:
    emoji = "\U0001F9CA"


tweet = emoji + "The weather right now in Chapel Hill today is " + temperature + degree_sign +"F. " + today

#tweet  = "The weather in Chapel Hill today is " + temperature + degree_sign +"F. " + today + summary  #sunriseTime + sunsetTime + moonPhase + summary 

if len(tweet) >140:
    emoji + "The weather right now in Chapel Hill today is " + temperature + degree_sign + "F. " + today



print(tweet)
print(emoji)

#This tweets it out
api.update_status(status = tweet)


