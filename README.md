# Movie Recommender

A web application that recommends movies and TV shows based on user preferences and filters.

## Features

- Browse movies and TV shows
- Filter by genre, year, and rating
- Get personalized recommendations
- Save favorites and create watchlists
- Detailed information about movies and shows
- IMDB integration for ratings and reviews

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
movie_recommender/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── models/           # Database models
└── utils/            # Utility functions
```

## Technologies Used

- Flask
- SQLAlchemy
- BeautifulSoup4
- Bootstrap 5
- JavaScript

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 