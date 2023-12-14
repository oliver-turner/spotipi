#!/usr/bin/env python
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from PiicoDev_Unified import sleep_ms

DEVICE_ID=os.getenv('MY_DEVICE_ID')
CLIENT_ID=os.getenv('MY_CLIENT_ID')
CLIENT_SECRET=os.getenv('MY_CLIENT_SECRET')

spotifyAuth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri="https://google.com/",
                                                        scope="user-read-playback-state,user-modify-playback-state",
                                                        open_browser=False))

spotifyAuth.transfer_playback(device_id=DEVICE_ID, force_play=False)

spotifyAuth.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1elGwF4VwkwglV4nCBPJtv'])
