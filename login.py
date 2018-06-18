from bottle import route, run, request
import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '1d464c3f15a2492da99afff5c6c65523'
SPOTIPY_CLIENT_SECRET = '94b549087ab04637b3f5fe64974df6ef'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# token = util.prompt_for_user_token('erfaniaa', scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri='http://localhost/')

# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print track['name'] + ' - ' + track['artists'][0]['name']
# else:
#     print "Can't get token for", username

# print(sp.new_releases()["albums"]["items"][1]["external_urls"]["spotify"])
print(len(sp.new_releases()["albums"]["items"]))
# print(sp.new_releases()["tracks"]["items"][1]["external_urls"]["spotify"])