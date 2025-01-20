import imdb
import random

# Initialize IMDb instance
ia = imdb.IMDb()

# List of available genres
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi']

# Function to recommend a movie based on genre
def recommend_movie(genre):
    # Search for movies using a keyword related to the genre
    search_results = ia.search_movie(genre)
    genre_movies = []
    for movie in search_results:
        try:
            ia.update(movie, info=['main'])
            if genre.lower() in (g.lower() for g in movie.get('genres', [])):
                genre_movies.append(movie)
        except Exception as e:
            continue
    if not genre_movies:
        return "No movies found for this genre."
    # Randomly select a movie
    movie = random.choice(genre_movies)
    return movie['title']

# Main function to run the chatbot
if __name__ == "__main__":
    while True:
        print("Select a genre from the following list:")
        for i, genre in enumerate(genres, 1):
            print(f"{i}. {genre}")
        print("0. Exit")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice == 0:
                print("Exiting the chatbot. Goodbye!")
                break
            elif 1 <= choice <= len(genres):
                selected_genre = genres[choice - 1]
                print(f"Recommended movie: {recommend_movie(selected_genre)}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
