import requests
import time
from app import app, db
from models import Movie

OMDB_API_KEY = "YOUR_OMDB_API_KEY"  # You'll need to get this from http://www.omdbapi.com/
BASE_URL = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}"

def fetch_movie_details(imdb_id):
    response = requests.get(f"{BASE_URL}&i={imdb_id}&plot=full")
    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            return {
                'title': data.get('Title'),
                'year': int(data.get('Year', '0').split('–')[0]),
                'genre': data.get('Genre'),
                'rating': float(data.get('imdbRating', '0')),
                'description': data.get('Plot'),
                'image_url': data.get('Poster'),
                'imdb_id': imdb_id,
                'director': data.get('Director'),
                'cast': data.get('Actors'),
                'runtime': int(data.get('Runtime', '0').split()[0]),
                'language': data.get('Language'),
                'popularity_score': float(data.get('imdbVotes', '0').replace(',', '')) / 100000
            }
    return None

def fetch_top_movies():
    # List of IMDb IDs for top movies (you can expand this list)
    top_movie_ids = [
        'tt0111161', 'tt0068646', 'tt0071562', 'tt0468569', 'tt0050083',
        'tt0108052', 'tt0167260', 'tt0110912', 'tt0060196', 'tt0120737',
        'tt0109830', 'tt0137523', 'tt0167261', 'tt0080684', 'tt0133093',
        'tt0099685', 'tt0073486', 'tt0047478', 'tt0114369', 'tt0118799',
        'tt0317248', 'tt0076759', 'tt0102926', 'tt0038650', 'tt0208092',
        'tt0120815', 'tt0245429', 'tt0110357', 'tt0120689', 'tt0816692',
        'tt0114814', 'tt0056058', 'tt0110413', 'tt0120586', 'tt0253474',
        'tt0088763', 'tt0103064', 'tt0027977', 'tt0054215', 'tt0120815',
        'tt0021749', 'tt0095765', 'tt0064116', 'tt0034583', 'tt0047396',
        'tt0095327', 'tt0078788', 'tt0082971', 'tt0032553', 'tt0033467'
    ]

    with app.app_context():
        for imdb_id in top_movie_ids:
            # Check if movie already exists
            if not Movie.query.filter_by(imdb_id=imdb_id).first():
                movie_data = fetch_movie_details(imdb_id)
                if movie_data:
                    movie = Movie(**movie_data)
                    db.session.add(movie)
                    print(f"Added: {movie_data['title']}")
                    time.sleep(1)  # Rate limiting
        
        db.session.commit()
        print("Finished fetching movies!")

if __name__ == '__main__':
    fetch_top_movies() 