import pandas as pd
import requests
import numpy as np
import json


url = "https://api.spotify.com/v1/playlists/6sJaRzQ7VJ5iNG4NYo58Db/tracks?fields=items(track(name)%2Ctrack(artists(name)))"

headers = {

}

track_name = []
artist_name = []