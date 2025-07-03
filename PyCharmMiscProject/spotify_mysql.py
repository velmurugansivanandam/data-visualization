import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='109b39eb9dc64a9693fd52310b691c63',
    client_secret='4f0aa6eef8594e02ad6405f9492f96bf'
))

# MySQL Database Connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'spotify_db'
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read track URLs from file
file_path = "track_urls.txt"
with open(file_path, 'r') as file:
    track_urls = file.readlines()

# Process each URL
for track_url in track_urls:
    track_url = track_url.strip()  # Remove any leading/trailing whitespace
    try:
        # Extract track ID from URL
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)# Fetch track details from Spotify API
        track = sp.track(track_id)

        # Extract metadata
        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }

        # Insert data into MySQL
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))
        connection.commit()
        print(f"Inserted: {track_data['Track Name']} by {track_data['Artist']}")
    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")
cursor.close()
connection.close()
print("All tracks have been processed and inserted into the database.")