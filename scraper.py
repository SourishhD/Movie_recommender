import requests
from bs4 import BeautifulSoup
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, app
from models import Movie
import time
import random

def scrape_imdb_movies(num_pages=2):
    base_url = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count=50"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    with app.app_context():
        for page in range(num_pages):
            try:
                url = f"{base_url}&start={1 + (page * 50)}"
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                movie_items = soup.find_all('div', class_='lister-item-content')
                
                for item in movie_items:
                    try:
                        # Extract movie details
                        title = item.find('h3', class_='lister-item-header').a.text.strip()
                        year_elem = item.find('span', class_='lister-item-year')
                        year = int(year_elem.text.strip('()').strip('I ').strip('–')) if year_elem else None
                        
                        # Get IMDB ID from the href
                        imdb_id = item.find('h3', class_='lister-item-header').a['href'].split('/')[2]
                        
                        # Check if movie already exists
                        if Movie.query.filter_by(imdb_id=imdb_id).first():
                            continue
                        
                        # Get rating
                        rating_elem = item.find('div', class_='ratings-imdb-rating')
                        rating = float(rating_elem['data-value']) if rating_elem else None
                        
                        # Get genre
                        genre_elem = item.find('span', class_='genre')
                        genre = genre_elem.text.strip() if genre_elem else None
                        
                        # Get description
                        desc_elem = item.find_all('p', class_='text-muted')
                        description = desc_elem[1].text.strip() if len(desc_elem) > 1 else None
                        
                        # Get image URL from the parent container
                        img_container = item.find_previous_sibling('div', class_='lister-item-image')
                        if img_container:
                            img_elem = img_container.find('img')
                            image_url = img_elem['src'] if img_elem else None
                        else:
                            image_url = None
                        
                        # Create new movie object
                        movie = Movie(
                            title=title,
                            year=year,
                            genre=genre,
                            rating=rating,
                            description=description,
                            image_url=image_url,
                            imdb_id=imdb_id
                        )
                        
                        db.session.add(movie)
                        print(f"Added: {title} ({year})")
                        
                    except Exception as e:
                        print(f"Error processing movie: {e}")
                        continue
                
                db.session.commit()
                print(f"Completed page {page + 1}")
                
                # Add delay between requests
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"Error processing page {page + 1}: {e}")
                continue

if __name__ == "__main__":
    scrape_imdb_movies() 