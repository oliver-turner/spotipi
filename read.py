#!/usr/bin/env python
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

rfid = PiicoDev_RFID()

DEVICE_ID=os.getenv('MY_DEVICE_ID')
CLIENT_ID=os.getenv('MY_CLIENT_ID')
CLIENT_SECRET=os.getenv('MY_CLIENT_SECRET')

spotifyAuth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri="https://google.com/",
                                                        scope="user-read-playback-state, user-modify-playback-state, useropen_browser=False"))


#print('Place tag near the RFID Module')
#
#while True:
#    if rfid.tagPresent():
#       id = rfid.readID()
#       id = rfid.readID(detail=True)
#
#       print(id)
#
#    sleep_ms(100)
