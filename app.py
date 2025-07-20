from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Mood-to-song mapping (more songs added)
mood_song_map = {
    "happy": [
        {"title": "Happy", "artist": "Pharrell Williams", "url": "https://open.spotify.com/track/60nZcImufyMA1MKQY3dcCH", "source": "Spotify"},
        {"title": "Can’t Stop the Feeling!", "artist": "Justin Timberlake", "url": "https://open.spotify.com/track/6JV2JOEocMgcZxYSZelKcc", "source": "Spotify"},
        {"title": "Good Life", "artist": "OneRepublic", "url": "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a", "source": "Spotify"},
        {"title": "Best Day of My Life", "artist": "American Authors", "url": "https://open.spotify.com/track/4dGrvB8ApjJqzTz6vX64gS", "source": "Spotify"},
        {"title": "On Top of the World", "artist": "Imagine Dragons", "url": "https://open.spotify.com/track/3k79jB5J0l0Xji1kLz3Gx5", "source": "Spotify"},
    ],
    "sad": [
        {"title": "Someone Like You", "artist": "Adele", "url": "https://open.spotify.com/track/4kflIGfjdZJW4ot2ioixTB", "source": "Spotify"},
        {"title": "Let Her Go", "artist": "Passenger", "url": "https://open.spotify.com/track/1tNJrcVe6gwLEiZCtprs1u", "source": "Spotify"},
        {"title": "Stay With Me", "artist": "Sam Smith", "url": "https://open.spotify.com/track/3RwexZgydFFvcVgRz0Qsn1", "source": "Spotify"},
        {"title": "Fix You", "artist": "Coldplay", "url": "https://open.spotify.com/track/6YndBU5cnhz0z6T6ssXGbD", "source": "Spotify"},
        {"title": "Say Something", "artist": "A Great Big World", "url": "https://open.spotify.com/track/2zzbO2xUFO4v8LFCM4EOLH", "source": "Spotify"},
    ],
    "energetic": [
        {"title": "Titanium", "artist": "David Guetta ft. Sia", "url": "https://open.spotify.com/track/3eR23VReFzcdmS7TYCrhCe", "source": "Spotify"},
        {"title": "Stronger", "artist": "Kanye West", "url": "https://open.spotify.com/track/2cYqizR4lgvp4Qu6IQ3qGN", "source": "Spotify"},
        {"title": "Eye of the Tiger", "artist": "Survivor", "url": "https://open.spotify.com/track/2KH16WveTQWT6KOG9Rg6e2", "source": "Spotify"},
        {"title": "Believer", "artist": "Imagine Dragons", "url": "https://open.spotify.com/track/0pqnGHJpmpxLKifKRmU6WP", "source": "Spotify"},
        {"title": "Don't Stop Me Now", "artist": "Queen", "url": "https://open.spotify.com/track/5e9TFTbltYBg2xThimr0rU", "source": "Spotify"},
    ],
    "focused": [
        {"title": "Weightless", "artist": "Marconi Union", "url": "https://open.spotify.com/track/6QPKYGnAW9QozVz2dSWqRg", "source": "Spotify"},
        {"title": "Intro", "artist": "The xx", "url": "https://open.spotify.com/track/1G391cbiT3v3Cywg8T7DM1", "source": "Spotify"},
        {"title": "Sunset Lover", "artist": "Petit Biscuit", "url": "https://open.spotify.com/track/0MOjJgT5BVQxvvz5IJ4j8J", "source": "Spotify"},
        {"title": "Night Owl", "artist": "Galimatias", "url": "https://open.spotify.com/track/6r26e6xzjLbgsW02WZ5CzP", "source": "Spotify"},
        {"title": "Cold Little Heart", "artist": "Michael Kiwanuka", "url": "https://open.spotify.com/track/5cYXeXYI8CEu0dclF8xOkg", "source": "Spotify"},
    ],
    "calm": [
        {"title": "River Flows in You", "artist": "Yiruma", "url": "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf", "source": "Spotify"},
        {"title": "Bloom", "artist": "The Paper Kites", "url": "https://open.spotify.com/track/2Lf3q2zknBjGHqcAq4lsNi", "source": "Spotify"},
        {"title": "Experience", "artist": "Ludovico Einaudi", "url": "https://open.spotify.com/track/4eLpB0IWmJRN7kUi5M2JCM", "source": "Spotify"},
        {"title": "Clair de Lune", "artist": "Debussy", "url": "https://open.spotify.com/track/0VdZ2F2r5jZFfGzi1Wxz1O", "source": "Spotify"},
        {"title": "Opus 55", "artist": "Joep Beving", "url": "https://open.spotify.com/track/0BQOIVhU6NbFl6jPXxwQuR", "source": "Spotify"},
    ],
    "anxious": [
        {"title": "Let It Be", "artist": "The Beatles", "url": "https://open.spotify.com/track/7iN1s7xHE4ifF5povM6A48", "source": "Spotify"},
        {"title": "Holocene", "artist": "Bon Iver", "url": "https://open.spotify.com/track/3xjCCh2aRgRiN8P5FwMfIP", "source": "Spotify"},
        {"title": "Lost in Japan", "artist": "Shawn Mendes", "url": "https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK", "source": "Spotify"},
        {"title": "The Night We Met", "artist": "Lord Huron", "url": "https://open.spotify.com/track/3QnPz7DqI9F9Wfc5UIN1kf", "source": "Spotify"},
        {"title": "Lovely", "artist": "Billie Eilish & Khalid", "url": "https://open.spotify.com/track/0u2P5u6lvoDfwTYjAADbn4", "source": "Spotify"},
    ],
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_mood = None
    songs = []

    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            prompt = data.get("prompt", "").lower()

            # Mood detection from prompt
            if "happy" in prompt:
                mood = "happy"
            elif "sad" in prompt:
                mood = "sad"
            elif "energetic" in prompt:
                mood = "energetic"
            elif "focused" in prompt:
                mood = "focused"
            elif "calm" in prompt:
                mood = "calm"
            elif "anxious" in prompt or "nervous" in prompt:
                mood = "anxious"
            else:
                mood = "happy"  # default

            return jsonify({"detected_mood": mood})
        else:
            selected_mood = request.form.get("mood")
            if selected_mood in mood_song_map:
                songs = random.sample(mood_song_map[selected_mood], k=5)

    return render_template("index.html", songs=songs, selected_mood=selected_mood)

if __name__ == "__main__":
    app.run(debug=True)
