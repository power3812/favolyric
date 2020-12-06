import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from google.colab import files

client_id                  = '2a11db57222c493993a206225d7e5475'
client_secret              = '7e7f3ead689f4e169129ad1eed2cbccf'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify                    = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# PandasでCSVを読み込む、最初の行は省略
songs = pd.read_csv("regional-jp-weekly-latest.csv", index_col = 0, header = 1)
songs.head(10)

# インデックスをリセットし、振り直す
songs = songs.reset_index()
songs.head(10)

song_info = pd.DataFrame()

# 楽曲数分の情報を取得
for url in songs["URL"]:
    df = pd.DataFrame.from_dict(spotify.audio_features(url))
    song_info = song_info.append(df)
song_info.head(10)

# song_infoのインデックスを振り直す
song_info = song_info.reset_index(drop = True)
song_info.head(10)

pd.concat([songs, song_info], axis = 1).to_csv("songs.csv")
