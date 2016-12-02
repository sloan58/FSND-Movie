import media
import fresh_tomatoes

# Create our movie_data details list.
movie_data = [
    [
        "No Retreat, No Surrender",
        "Train with the ghost of Bruce Lee",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwMDYyMDU4MV5BMl5BanBnXkFtZTcwOTUwNTYyMQ@@._V1_.jpg",
        "https://www.youtube.com/watch?v=4zYgAGt3bps"
    ],
    [
        "Rocky III",
        "Mr T!",
        # The next url is too long per PEP8 but I think it's okay in this case...
        # https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyOTYzMDMzMF5BMl5BanBnXkFtZTcwMTkzODM1NA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=gbRDCWKqvEc"
    ],
    [
        "Top Gun",
        "The Top Gun Naval Fighter Weapons School",
        "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",
        "https://www.youtube.com/watch?v=qAfbp3YX9F0"
    ],

]

# Create an empty list to hold Movie objects.
movie_objects = []

# Iterate movie_data and create new Movie objects.
for movie in movie_data:

    # Create a new Movie object and append it to movie_objects.
    movie_objects.append(media.Movie(movie[0], movie[1], movie[2], movie[3]))

# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movie_objects)
