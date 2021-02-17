from flask import Flask, render_template
import requests
import os
import random
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

load_dotenv(find_dotenv())

#Personal client credentials to access the API
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

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
TRACK_ID_LIST = ['1y4jsQt7MjnZhiD1L6qFBC', '1kd5qplldnxu16qcZXS3Yk', '5fbSIKNisMBlP1tXxjziJb', '6ZVuGZvrViwA5uliEQ4F7Y', '3ZYN2cfyCFn4NuWxEW9tuh', '3yOlyBJuViE2YSGn3nVE1K', '6SRWhUJcD2YKahCwHavz3X']
TRACK_ID = random.choice(TRACK_ID_LIST)

@app.route('/')
def get_song_info():
    r = requests.get(BASE_SPT + 'tracks/' + TRACK_ID, headers=headers)
    request = r.json()
    genius_url = 'http://api.genius.com/search'
    GENIUS_TOKEN = os.getenv('GENIUS_TOKEN')
    genius_header = {'Authorization': 'BEARER {token}'.format(token=GENIUS_TOKEN)}
    song_title = request['name']
    params = {'q': song_title}
    s = requests.get(genius_url, params=params, headers=genius_header)
    response = s.json()
    song_lyrics_url = "No Lyrics exist"
    for hit in response['response']['hits']:
        if hit['result']['primary_artist']['name'].lower() == request['album']['artists'][0]['name'].lower():
            song_lyrics_url = hit['result']['url']
            break
    return render_template(
        "index.html",
        lyric_link = song_lyrics_url,
        artist_name = request['album']['artists'][0]['name'],
        song_name = request['name'],
        preview_url = request['preview_url'],
        image_src = request['album']['images'][1]['url'])


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)