import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PiicoDev_Unified import sleep_ms

DEVICE_ID='MY_DEVICE_ID'
CLIENT_ID='MY_CLIENT_ID'
CLIENT_SECRET='MY_CLIENT_SECRET'

spotifyAuth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri="http://localhost:8080",
                                                        scope="user-read-playback-state,user-modify-playback-state"))

spotifyAuth.transfer_playback(device_id=DEVICE_ID, force_play=False)

spotifyAuth.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1elGwF4Vwkwg1V4nCBPJtv'])
