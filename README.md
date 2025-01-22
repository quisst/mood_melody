# Mood Melody

Mood Melody is a web application that recommends personalized music playlists based on your mood and preferences. Users can input their daily diary, select their preferred genre, song duration, year range, and mood to receive a customized playlist from Spotify.  

## Features
- **User-friendly input form** with mood, genre, and duration selection.  
- **Sentiment analysis** of diary entries (Positive, Negative, Neutral).  
- **Personalized playlist recommendations** based on mood, genre, and preferences.  
- **Spotify integration** to fetch and display songs with album art and artist details.  
- **Responsive design** for an enhanced user experience.  

## Technologies Used
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS  
- **APIs:** Spotify API for music recommendations  
- **AI:** KoBERT for sentiment analysis  
- **Version Control:** Git & GitHub  

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/quisst/mood-melody.git
   cd mood-melody
   ```
   
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Set up environment variables:**
  Create a .env file in the project root and add the following:
   ```env
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=your_redirect_uri
   SECRET_KEY=your_django_secret_key
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    
7. **Access the application:**
    Open your browser and visit http://127.0.0.1:8000.


# Usage
1. Enter your diary entry in the provided text area.
2. Choose your preferred **genre**, **mood**, **song duration**, and **year range**.
3. Click on the **"Get Recommendations"** button.
4. View the recommended songs with album cover, artist name, and song title.
5. Click the song link to listen on Spotify.


# Project Structure
```
mood-melody/
│-- recommendations/
│   ├── migrations/
│   ├── static/
│   │   ├── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── results.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│-- mood_melody/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── __init__.py
│-- .env
│-- .gitignore
│-- db.sqlite3
│-- manage.py
│-- requirements.txt
│-- README.md
```
