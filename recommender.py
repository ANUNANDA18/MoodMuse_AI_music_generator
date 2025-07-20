# recommender.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

mood_to_genre = {
    "happy": "pop",
    "sad": "acoustic",
    "energetic": "edm",
    "focused": "lo-fi"
}

def get_songs_for_mood(mood):
    genre = mood_to_genre.get(mood, "pop")
    results = sp.search(q=f"genre:{genre}", type="track", limit=5)
    songs = []
    for track in results['tracks']['items']:
        songs.append({
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify']
        })
    return songs

