from flask import Flask, render_template
import requests
import os
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Personal client credentials to access the API
CLIENT_ID = 'ec2f029b0f0e4d30a67884900d9f53b6'
CLIENT_SECRET = '7089726d89be40fcbf15f8e24b3751f5'

#Storing response from the server using POST
AUTH_RSP = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type':'client_credentials',
    'client_id':CLIENT_ID,
    'client_secret':CLIENT_SECRET
})
AUTH_RESPONSE = AUTH_RSP.json()
 
#Formatting API requests to remove clutter and improve readability
ACCESS_TK = AUTH_RESPONSE['access_token']
headers = { 'Authorization': 'Bearer {token}'.format(token=ACCESS_TK) }
BASE_SPT = 'https://api.spotify.com/v1/'

#Chooses a random track from a list of recent favorites
TRACK_ID_LIST = ['1y4jsQt7MjnZhiD1L6qFBC', '1kd5qplldnxu16qcZXS3Yk', '4FHhXviyyftv946wV4I5P5', '6ZVuGZvrViwA5uliEQ4F7Y', '0ytvsZOerGzUWfHXVT2Sgy', '3yOlyBJuViE2YSGn3nVE1K']
TRACK_ID = random.choice(TRACK_ID_LIST)

@app.route('/')
def get_song_info():
    r = requests.get(BASE_SPT + 'tracks/' + TRACK_ID, headers=headers)
    request = r.json()
    genius_url = 'http://api.genius.com/search'
    genius_header = {'Authorization': 'BEARER QW7LEM7QIeuuZlKcb4kWsy7Q9Z7ECUNKCsiRyvZNXICUi1a1758J_bDydLEOk5gx'}
    song_title = request['name']
    params = {'q': song_title}
    s = requests.get(genius_url, params=params, headers=genius_header)
    response = s.json()
    song_lyrics_url = "No Lyrics exist"
    for hit in response['response']['hits']:
        if hit['result']['primary_artist']['name'].lower() == request['album']['artists'][0]['name'].lower():
            song_lyrics_url = hit['result']['url']
            break
    print(song_lyrics_url)
    return render_template(
        "index.html",
        artist_name = request['album']['artists'][0]['name'],
        song_name = request['name'],
        preview_url = request['preview_url'],
        image_src = request['album']['images'][1]['url'])


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)