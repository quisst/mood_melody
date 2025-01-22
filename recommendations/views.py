from django.shortcuts import render, redirect
from django.conf import settings
from spotipy.oauth2 import SpotifyOAuth
from .forms import MoodForm
from .utils import get_spotify_recommendations, analyze_mood, authenticate_spotify

def index(request):
    form = MoodForm()
    return render(request, 'index.html', {'form': form})

def recommend(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            return redirect('spotify_callback')
    return redirect('index')

def spotify_callback(request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIPY_CLIENT_ID,
        client_secret=settings.SPOTIPY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIPY_REDIRECT_URI,
        scope="user-library-read playlist-modify-public"
    )
    code = request.GET.get('code')
    token_info = sp_oauth.get_access_token(code)
    
    if token_info:
        request.session['spotify_token'] = token_info['access_token']
        form_data = request.session.pop('form_data', None)
        if form_data:
            diary_entry = form_data['diary_entry']
            genre = form_data['genre']
            duration = form_data['duration']
            year_range = form_data['year_range']
            mood = form_data['mood']
            
            sentiment = analyze_mood(diary_entry)
            sp = authenticate_spotify()
            recommendations = get_spotify_recommendations(sp, sentiment, genre, duration, year_range, mood)
            return render(request, 'results.html', {
                'sentiment': sentiment,
                'recommendations': recommendations,
            })
    return redirect('index')