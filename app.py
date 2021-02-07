from flask import Flask, render_template
import requests
import spotipy
import os
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

CLIENT_ID = 'ec2f029b0f0e4d30a67884900d9f53b6'
CLIENT_SECRET = '7089726d89be40fcbf15f8e24b3751f5'
AUTH_TK_URL = 'https://accounts.spotify.com/api/token'

AUTH_RSP = requests.post(AUTH_TK_URL, {
    'grant_type':'client_credentials',
    'client_id':CLIENT_ID,
    'client_secret':CLIENT_SECRET
})
AUTH_RESPONSE = AUTH_RSP.json()
ACCESS_TK = AUTH_RESPONSE['access_token']

headers = { 'Authorization': 'Bearer {token}'.format(token=ACCESS_TK) }

BASE = 'https://api.spotify.com/v1/'

TRACK_ID_LIST = ['0u2P5u6lvoDfwTYjAADbn4', '1kd5qplldnxu16qcZXS3Yk', '4FHhXviyyftv946wV4I5P5', '3Wn52FjoUJClQOXwKePPp3', '0ytvsZOerGzUWfHXVT2Sgy']
TRACK_ID = random.choice(TRACK_ID_LIST)

@app.route('/')
def get_song_info():
    r = requests.get(BASE + 'tracks/' + TRACK_ID, headers=headers)
    request = r.json()
    return render_template(
        "index.html",
        artist_name = request['album']['artists'][0]['name'],
        song_name = request['album']['name'],
        preview_url = request['preview_url'],
        image_src = request['album']['images'][1]['url'])


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)