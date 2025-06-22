from app import app, db
from models import Movie, Actor

def init_db():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create tables
        db.create_all()
        
        # Add sample movies with complete information
        sample_movies = [
            {
                'title': 'The Shawshank Redemption',
                'year': 1994,
                'genre': 'Drama',
                'rating': 9.3,
                'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'runtime': 142,
                'director': 'Frank Darabont',
                'writer': 'Stephen King (short story), Frank Darabont (screenplay)',
                'music_director': 'Thomas Newman',
                'cinematographer': 'Roger Deakins',
                'trailer_url': 'https://www.youtube.com/embed/6hB3S9bIaco',
                'cast': [
                    {'name': 'Tim Robbins', 'character': 'Andy Dufresne', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTI1OTYxNzAxOF5BMl5BanBnXkFtZTYwNTE5ODI4._V1_UY317_CR16,0,214,317_AL_.jpg'},
                    {'name': 'Morgan Freeman', 'character': 'Ellis Boyd "Red" Redding', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTc0MDMyMzI2OF5BMl5BanBnXkFtZTcwMzM2OTk1MQ@@._V1_UY317_CR7,0,214,317_AL_.jpg'},
                    {'name': 'Bob Gunton', 'character': 'Warden Norton', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjUyZDQ0NjktZmM5YS00YzBkLTg5NGEtZjJhZTE0OTQ5YmRjXkEyXkFqcGdeQXVyMTI3MDk3MzQ@._V1_UY317_CR10,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'The Dark Knight',
                'year': 2008,
                'genre': 'Action, Crime, Drama',
                'rating': 9.0,
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg',
                'runtime': 152,
                'director': 'Christopher Nolan',
                'writer': 'Jonathan Nolan, Christopher Nolan',
                'music_director': 'Hans Zimmer, James Newton Howard',
                'cinematographer': 'Wally Pfister',
                'trailer_url': 'https://www.youtube.com/embed/EXeTwQWrcwY',
                'cast': [
                    {'name': 'Christian Bale', 'character': 'Bruce Wayne / Batman', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTkxMzk4MjQ4MF5BMl5BanBnXkFtZTcwMzExODQxOA@@._V1_UY317_CR4,0,214,317_AL_.jpg'},
                    {'name': 'Heath Ledger', 'character': 'Joker', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTI2NTY0NzA4MF5BMl5BanBnXkFtZTYwMjE1MDE0._V1_UX214_CR0,0,214,317_AL_.jpg'},
                    {'name': 'Aaron Eckhart', 'character': 'Harvey Dent', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTc4MTAyNzMzNF5BMl5BanBnXkFtZTcwMzQ5MzQzMg@@._V1_UY317_CR6,0,214,317_AL_.jpg'},
                    {'name': 'Michael Caine', 'character': 'Alfred', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjAwNzIwNTQ4Ml5BMl5BanBnXkFtZTYwMzE1MTUz._V1_UY317_CR7,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'Inception',
                'year': 2010,
                'genre': 'Action, Adventure, Sci-Fi',
                'rating': 8.8,
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg',
                'runtime': 148,
                'director': 'Christopher Nolan',
                'writer': 'Christopher Nolan',
                'music_director': 'Hans Zimmer',
                'cinematographer': 'Wally Pfister',
                'trailer_url': 'https://www.youtube.com/embed/YoHD9XEInc0',
                'cast': [
                    {'name': 'Leonardo DiCaprio', 'character': 'Cobb', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjI0MTg3MzI0M15BMl5BanBnXkFtZTcwMzQyODU2Mw@@._V1_UY317_CR10,0,214,317_AL_.jpg'},
                    {'name': 'Joseph Gordon-Levitt', 'character': 'Arthur', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTQzOTg0NTU4NF5BMl5BanBnXkFtZTcwNTQ4MTcwOQ@@._V1_UY317_CR35,0,214,317_AL_.jpg'},
                    {'name': 'Ellen Page', 'character': 'Ariadne', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTU3MzM3MDYzMV5BMl5BanBnXkFtZTcwNzk1Mzc3NA@@._V1_UY317_CR6,0,214,317_AL_.jpg'},
                    {'name': 'Tom Hardy', 'character': 'Eames', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTQ3ODEyNjA4Nl5BMl5BanBnXkFtZTgwMTE4ODMyMjE@._V1_UX214_CR0,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'The Godfather',
                'year': 1972,
                'genre': 'Crime, Drama',
                'rating': 9.2,
                'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'runtime': 175,
                'director': 'Francis Ford Coppola',
                'writer': 'Mario Puzo, Francis Ford Coppola',
                'music_director': 'Nino Rota',
                'cinematographer': 'Gordon Willis',
                'trailer_url': 'https://www.youtube.com/embed/sY1S34973zA',
                'cast': [
                    {'name': 'Marlon Brando', 'character': 'Don Vito Corleone', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTg3MDYyMDE5OF5BMl5BanBnXkFtZTcwNjgyNTEzNA@@._V1_UY317_CR97,0,214,317_AL_.jpg'},
                    {'name': 'Al Pacino', 'character': 'Michael Corleone', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTQzMzg1ODAyNl5BMl5BanBnXkFtZTYwMjAxODQ1._V1_UX214_CR0,0,214,317_AL_.jpg'},
                    {'name': 'James Caan', 'character': 'Sonny Corleone', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTI5NjkyNDQ3NV5BMl5BanBnXkFtZTcwNjY5NTQ0Mw@@._V1_UY317_CR7,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'Pulp Fiction',
                'year': 1994,
                'genre': 'Crime, Drama',
                'rating': 8.9,
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'runtime': 154,
                'director': 'Quentin Tarantino',
                'writer': 'Quentin Tarantino',
                'music_director': 'Various Artists',
                'cinematographer': 'Andrzej Sekula',
                'trailer_url': 'https://www.youtube.com/embed/s7EdQ4FqbhY',
                'cast': [
                    {'name': 'John Travolta', 'character': 'Vincent Vega', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTUwNjQ0ODkxN15BMl5BanBnXkFtZTcwMDc5NjQwNw@@._V1_UY317_CR11,0,214,317_AL_.jpg'},
                    {'name': 'Samuel L. Jackson', 'character': 'Jules Winnfield', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTQ1NTQwMTYxNl5BMl5BanBnXkFtZTYwMjA1MzY1._V1_UX214_CR0,0,214,317_AL_.jpg'},
                    {'name': 'Uma Thurman', 'character': 'Mia Wallace', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjMxNzk1MTQyMl5BMl5BanBnXkFtZTgwMDIzMDEyMTE@._V1_UX214_CR0,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'Forrest Gump',
                'year': 1994,
                'genre': 'Drama, Romance',
                'rating': 8.8,
                'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
                'runtime': 142,
                'director': 'Robert Zemeckis',
                'writer': 'Winston Groom, Eric Roth',
                'music_director': 'Alan Silvestri',
                'cinematographer': 'Don Burgess',
                'trailer_url': 'https://www.youtube.com/embed/bLvqoHBptjg',
                'cast': [
                    {'name': 'Tom Hanks', 'character': 'Forrest Gump', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTQ2MjMwNDA3Nl5BMl5BanBnXkFtZTcwMTA2NDY3NQ@@._V1_UY317_CR2,0,214,317_AL_.jpg'},
                    {'name': 'Robin Wright', 'character': 'Jenny Curran', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTU0NTc4MzEyOV5BMl5BanBnXkFtZTcwODY0ODkzMQ@@._V1_UY317_CR4,0,214,317_AL_.jpg'},
                    {'name': 'Gary Sinise', 'character': 'Lieutenant Dan Taylor', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTg3MjgxMjQxNl5BMl5BanBnXkFtZTcwOTQ1MjAwNA@@._V1_UY317_CR10,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'The Matrix',
                'year': 1999,
                'genre': 'Action, Sci-Fi',
                'rating': 8.7,
                'description': 'A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg',
                'runtime': 136,
                'director': 'Lana Wachowski, Lilly Wachowski',
                'writer': 'Lana Wachowski, Lilly Wachowski',
                'music_director': 'Don Davis',
                'cinematographer': 'Bill Pope',
                'trailer_url': 'https://www.youtube.com/embed/vKQi3bBA1y8',
                'cast': [
                    {'name': 'Keanu Reeves', 'character': 'Neo', 'image_url': 'https://m.media-amazon.com/images/M/MV5BNjUxNDcwMTg4Ml5BMl5BanBnXkFtZTcwMjU4NDYyOA@@._V1_UY317_CR15,0,214,317_AL_.jpg'},
                    {'name': 'Laurence Fishburne', 'character': 'Morpheus', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTc0NjczNDc1MV5BMl5BanBnXkFtZTYwMDU0Mjg1._V1_UX214_CR0,0,214,317_AL_.jpg'},
                    {'name': 'Carrie-Anne Moss', 'character': 'Trinity', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjExNzA4MDYxN15BMl5BanBnXkFtZTcwOTI1MDAxOQ@@._V1_UY317_CR14,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'Goodfellas',
                'year': 1990,
                'genre': 'Biography, Crime, Drama',
                'rating': 8.7,
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjIwYjFjNmI3ZGEwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'runtime': 146,
                'director': 'Martin Scorsese',
                'writer': 'Nicholas Pileggi, Martin Scorsese',
                'music_director': 'Various Artists',
                'cinematographer': 'Michael Ballhaus',
                'trailer_url': 'https://www.youtube.com/embed/qo5jJpHtI1Y',
                'cast': [
                    {'name': 'Robert De Niro', 'character': 'James Conway', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjAwNDU3MzcyOV5BMl5BanBnXkFtZTcwMjc0MTIxMw@@._V1_UY317_CR13,0,214,317_AL_.jpg'},
                    {'name': 'Ray Liotta', 'character': 'Henry Hill', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjE1NjQ5ODc2NV5BMl5BanBnXkFtZTcwMjE5NjQxMw@@._V1_UY317_CR5,0,214,317_AL_.jpg'},
                    {'name': 'Joe Pesci', 'character': 'Tommy DeVito', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMzc3MTcxNDYxNV5BMl5BanBnXkFtZTcwMjYzNzE2MQ@@._V1_UY317_CR8,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'Fight Club',
                'year': 1999,
                'genre': 'Drama',
                'rating': 8.8,
                'description': 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
                'runtime': 139,
                'director': 'David Fincher',
                'writer': 'Chuck Palahniuk, Jim Uhls',
                'music_director': 'The Dust Brothers',
                'cinematographer': 'Jeff Cronenweth',
                'trailer_url': 'https://www.youtube.com/embed/SUXWAEX2jlg',
                'cast': [
                    {'name': 'Brad Pitt', 'character': 'Tyler Durden', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjA1MjE2MTQ2MV5BMl5BanBnXkFtZTcwMjE5MDY0Nw@@._V1_UX214_CR0,0,214,317_AL_.jpg'},
                    {'name': 'Edward Norton', 'character': 'The Narrator', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTYwNjQ5MTI1NF5BMl5BanBnXkFtZTcwMzU5MTI2Mw@@._V1_UY317_CR16,0,214,317_AL_.jpg'},
                    {'name': 'Helena Bonham Carter', 'character': 'Marla Singer', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTUzMzUzMDg5MV5BMl5BanBnXkFtZTcwMzIxNTk3OA@@._V1_UY317_CR3,0,214,317_AL_.jpg'}
                ]
            },
            {
                'title': 'Interstellar',
                'year': 2014,
                'genre': 'Adventure, Drama, Sci-Fi',
                'rating': 8.6,
                'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
                'image_url': 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                'runtime': 169,
                'director': 'Christopher Nolan',
                'writer': 'Jonathan Nolan, Christopher Nolan',
                'music_director': 'Hans Zimmer',
                'cinematographer': 'Hoyte van Hoytema',
                'trailer_url': 'https://www.youtube.com/embed/zSWdZVtXT7E',
                'cast': [
                    {'name': 'Matthew McConaughey', 'character': 'Cooper', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTg0MDc3ODUwOV5BMl5BanBnXkFtZTcwMTk2NjY4Nw@@._V1_UX214_CR0,0,214,317_AL_.jpg'},
                    {'name': 'Anne Hathaway', 'character': 'Brand', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTRhNzQ3NGMtZmQ1Mi00ZTViLTk3OTgtOTk0YzE2YTgwMmFjXkEyXkFqcGdeQXVyNzg5MzIyOA@@._V1_UY317_CR20,0,214,317_AL_.jpg'},
                    {'name': 'Jessica Chastain', 'character': 'Murphy', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTU1MDM5NjczOF5BMl5BanBnXkFtZTcwOTY2MDE4OA@@._V1_UY317_CR31,0,214,317_AL_.jpg'}
                ]
            }
        ]
        
        for movie_data in sample_movies:
            cast_data = movie_data.pop('cast', [])
            movie = Movie(**movie_data)
            db.session.add(movie)
            db.session.flush()  # This assigns the movie.id
            
            for actor_data in cast_data:
                actor = Actor(movie_id=movie.id, **actor_data)
                db.session.add(actor)
        
        db.session.commit()
        print("Database initialized with sample movies!")

if __name__ == '__main__':
    init_db() 