# spotify_suggester.py
import os
from dotenv import load_dotenv

env_path = r"C:\Users\Anunanda\MoodMuse\.env"
print("DEBUG - .env path exists:", os.path.exists(env_path))
with open(env_path, "r") as f:
    print("DEBUG - .env content:\n", f.read())



# ✅ Correct dotenv path loading
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

print("DEBUG - CLIENT ID:", os.getenv("SPOTIPY_CLIENT_ID"))
print("DEBUG - CLIENT SECRET:", os.getenv("SPOTIPY_CLIENT_SECRET"))

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Read from environment variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# ✅ Check again here
if not client_id or not client_secret:
    raise Exception("SPOTIPY_CLIENT_ID or SPOTIPY_CLIENT_SECRET is not set")

# Initialize Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

def get_songs_by_mood(mood):
    query = f"{mood} music"
    results = sp.search(q=query, type='track', limit=10)
    songs = []

    for item in results['tracks']['items']:
        name = item['name']
        artist = item['artists'][0]['name']
        url = item['external_urls']['spotify']
        songs.append({'name': name, 'artist': artist, 'url': url})

    return songs
