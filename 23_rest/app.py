import urllib.request
import urllib.urlopen
import json

# with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY') as response:
#    html = response.read()


req = urllib.request.Request('https://api.nasa.gov/planetary/apod?api_key=5oi0NGdFzVgIvA23FdQS8YXx5OSInUPSOuhx88RC')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
