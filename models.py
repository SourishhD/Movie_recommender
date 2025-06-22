from database import db

class Actor(db.Model):
    __tablename__ = 'actors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    character = db.Column(db.String(100))
    image_url = db.Column(db.String(500))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    def __repr__(self):
        return f'<Actor {self.name}>'

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=True, default='https://via.placeholder.com/300x450?text=No+Image')
    imdb_id = db.Column(db.String(20))
    runtime = db.Column(db.Integer)
    director = db.Column(db.String(100))
    writer = db.Column(db.String(200))
    music_director = db.Column(db.String(100))
    cinematographer = db.Column(db.String(100))
    trailer_url = db.Column(db.String(500))
    cast = db.relationship('Actor', backref='movie', lazy=True)

    def __repr__(self):
        return f'<Movie {self.title}>'