#!/usr/bin/env python
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

DEVICE_ID=os.getenv('MY_DEVICE_ID')
CLIENT_ID=os.getenv('MY_CLIENT_ID')
CLIENT_SECRET=os.getenv('MY_CLIENT_SECRET')

while True:
    try:
        rfid = PiicoDev_RFID()
        spotifyAuth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri="https://google.com/",
                                                        scope="user-read-playback-state,user-modify-playback-state",
                                                        open_browser=False))

        print("Please scan a record you want to listen to :)")

        while True:
            if rfid.tagPresent():
                id = rfid.readID()
                print("You have scanned: ", id)
                spotifyAuth.transfer_playback(device_id=DEVICE_ID, force_play=False)
                if (id=="04:26:85:FA:3F:74:80"):
                    spotifyAuth.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4GKphhKJprqrPkLuU8Vsyu'])
                    sleep_ms(100)

    except Exception as e:
        print(e)
        pass

'''
print('Place tag near the RFID Module')

while True:
    if rfid.tagPresent():
       id = rfid.readID()
      # id = rfid.readID(detail=True)

       print(id)

    sleep_ms(100)
'''
