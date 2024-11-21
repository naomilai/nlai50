# Team: Oreo
# Naomi and Amanda
# November 20 2024

import urllib.request, json
from flask import Flask, render_template, request

# with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY') as response:
#    html = response.read()

app = Flask(__name__)

# req = urllib.request.Request('https://api.nasa.gov/planetary/apod?api_key=5oi0NGdFzVgIvA23FdQS8YXx5OSInUPSOuhx88RC')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()

@app.route("/")
def main():
   # test drive requests.get(), requests.get().json(), requests.urlopen()
   # test drive json.loads(), json.dumps()
   url = 'https://api.nasa.gov/planetary/apod?api_key='
   key = '5oi0NGdFzVgIvA23FdQS8YXx5OSInUPSOuhx88RC'

   request = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=5oi0NGdFzVgIvA23FdQS8YXx5OSInUPSOuhx88RC')
   response = request.read() # converts to json 
   data = json.loads(response) # converts json string to dictionary

   date = data['date']
   explanation = data['explanation']
   url = data['url']
   title = data['title']

   return render_template('main.html', title = title, url = url, explanation = explanation, date = date)

if __name__ == "__main__":
   app.debug = True 
   app.run()

