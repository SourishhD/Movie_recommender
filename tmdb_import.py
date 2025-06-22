import requests
import os
from app import app, db
from models import Movie, Actor
from datetime import datetime

# TMDb API configuration
TMDB_API_KEY = "95532abf1357d5c6d72638573435cb9a"  # TMDb API Key
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"

def get_movie_details(movie_id):
    """Fetch detailed movie information including credits"""
    # Get basic movie info
    movie_url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "append_to_response": "credits,videos"
    }
    
    response = requests.get(movie_url, params=params)
    if response.status_code != 200:
        return None
    
    movie_data = response.json()
    
    # Get trailer
    trailer_url = None
    if movie_data.get('videos') and movie_data['videos'].get('results'):
        for video in movie_data['videos']['results']:
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                trailer_url = f"https://www.youtube.com/embed/{video['key']}"
                break
    
    # Process cast
    cast = []
    if movie_data.get('credits') and movie_data['credits'].get('cast'):
        for actor in movie_data['credits']['cast'][:5]:  # Get top 5 cast members
            cast_member = {
                'name': actor['name'],
                'character': actor['character'],
                'image_url': f"{IMAGE_BASE_URL}{actor['profile_path']}" if actor['profile_path'] else None
            }
            cast.append(cast_member)
    
    # Get director and writer
    director = None
    writer = None
    if movie_data.get('credits') and movie_data['credits'].get('crew'):
        for crew_member in movie_data['credits']['crew']:
            if crew_member['job'] == 'Director':
                director = crew_member['name']
            elif crew_member['job'] == 'Screenplay':
                writer = crew_member['name']
    
    return {
        'title': movie_data['title'],
        'year': datetime.strptime(movie_data['release_date'], '%Y-%m-%d').year if movie_data.get('release_date') else None,
        'genre': ', '.join(genre['name'] for genre in movie_data['genres']),
        'rating': movie_data['vote_average'],
        'description': movie_data['overview'],
        'image_url': f"{IMAGE_BASE_URL}{movie_data['poster_path']}" if movie_data.get('poster_path') else None,
        'runtime': movie_data['runtime'],
        'director': director,
        'writer': writer,
        'trailer_url': trailer_url,
        'cast': cast
    }

def import_popular_movies(page_count=5):
    """Import popular movies from TMDb"""
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        movies_added = 0
        
        for page in range(1, page_count + 1):
            # Get popular movies
            popular_url = f"{BASE_URL}/movie/popular"
            params = {
                "api_key": TMDB_API_KEY,
                "page": page
            }
            
            response = requests.get(popular_url, params=params)
            if response.status_code != 200:
                print(f"Error fetching page {page}")
                continue
            
            movies = response.json()['results']
            
            for movie_data in movies:
                # Get detailed movie info
                movie_details = get_movie_details(movie_data['id'])
                if not movie_details:
                    continue
                
                # Create movie record
                cast_data = movie_details.pop('cast', [])
                movie = Movie(**movie_details)
                db.session.add(movie)
                db.session.flush()  # This assigns the movie.id
                
                # Add cast members
                for actor_data in cast_data:
                    actor = Actor(movie_id=movie.id, **actor_data)
                    db.session.add(actor)
                
                movies_added += 1
                print(f"Added: {movie_details['title']}")
            
            db.session.commit()
            print(f"Completed page {page}")
        
        print(f"\nTotal movies added: {movies_added}")

if __name__ == '__main__':
    import_popular_movies(page_count=15)  # Increased from 5 to 15 pages to get about 300 movies 