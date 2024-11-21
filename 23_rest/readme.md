## DISCO
1. key must be added to end of url
2. urllib.request.urlopen(url + key) gets the page
3. request.read() converts to json
4. json.loads(response) converts json string to dictionary

## QCC
1. why do we need a separate text file with key?
2. why is explanation not in query parameters online, but shows in the dictionary?
