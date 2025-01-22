import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from transformers import pipeline

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope='user-library-read playlist-modify-public'
    ))
    return sp

def analyze_mood(entry):
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    result = sentiment_pipeline(entry)
    sentiment_score = result[0]['label']
    if sentiment_score in ['1 star', '2 stars']:
        return "negative"
    elif sentiment_score in ['3 stars']:
        return "neutral"
    else:
        return "positive"

def get_spotify_recommendations(sp, sentiment, genre, duration, year_range, mood):
    query = f"{sentiment} {genre} {mood}"
    if year_range:
        query += f" year:{year_range}"
    
    final_tracks = []
    seen_track_ids = set()
    limit = 10
    max_attempts = 10
    attempts = 0

    while len(final_tracks) < 10 and attempts < max_attempts:
        results = sp.search(q=query, type='track', limit=limit, offset=attempts * limit)
        
        for track in results['tracks']['items']:
            track_id = track['id']
            if track_id not in seen_track_ids:
                duration_ms = track['duration_ms']
                if (duration == 'short' and duration_ms < 180000) or \
                   (duration == 'medium' and 180000 <= duration_ms <= 300000) or \
                   (duration == 'long' and duration_ms > 300000):
                    
                    final_tracks.append(track)
                    seen_track_ids.add(track_id)
                    
                    if len(final_tracks) == 10:
                        break

        attempts += 1
    
    return final_tracks

