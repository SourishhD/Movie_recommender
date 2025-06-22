from flask import Flask, render_template, request, jsonify, abort
from database import db
from models import Movie, Actor
import math

# Create Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie_detail.html', movie=movie)

@app.route('/api/movies')
def get_movies():
    # Get filter parameters
    genre = request.args.get('genre')
    rating = request.args.get('rating', type=float)
    year_from = request.args.get('year_from', type=int)
    year_to = request.args.get('year_to', type=int)
    
    # Get pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    
    # Start building the query
    query = Movie.query
    
    # Add filters to query
    if genre:
        genres = genre.split(',')
        genre_conditions = []
        for g in genres:
            genre_conditions.append(Movie.genre.ilike(f'%{g}%'))
        if genre_conditions:
            query = query.filter(db.or_(*genre_conditions))
    
    if rating is not None and rating > 0:
        query = query.filter(Movie.rating >= rating)
    
    if year_from:
        query = query.filter(Movie.year >= year_from)
    
    if year_to:
        query = query.filter(Movie.year <= year_to)
    
    # Get total count for pagination
    total_movies = query.count()
    
    # Add ordering and pagination
    query = query.order_by(Movie.rating.desc())
    movies = query.paginate(page=page, per_page=per_page, error_out=False)
    
    # Convert to list of dictionaries
    movies_list = []
    for movie in movies.items:
        movies_list.append({
            'id': movie.id,
            'title': movie.title,
            'year': movie.year,
            'rating': movie.rating,
            'genre': movie.genre,
            'description': movie.description,
            'image_url': movie.image_url,
            'runtime': movie.runtime,
            'director': movie.director,
            'writer': movie.writer,
            'music_director': movie.music_director,
            'cinematographer': movie.cinematographer,
            'trailer_url': movie.trailer_url
        })
    
    return jsonify({
        'movies': movies_list,
        'total': total_movies,
        'page': page,
        'per_page': per_page,
        'total_pages': math.ceil(total_movies / per_page)
    })

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True) 