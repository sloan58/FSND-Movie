import media
import fresh_tomatoes

movie_data = [
    ["No Retreat, No Surrender", "Train with the ghost of Bruce Lee", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwMDYyMDU4MV5BMl5BanBnXkFtZTcwOTUwNTYyMQ@@._V1_.jpg", "https://www.youtube.com/watch?v=4zYgAGt3bps"],
    ["Rocky III", "Mr T!", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyOTYzMDMzMF5BMl5BanBnXkFtZTcwMTkzODM1NA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg", "https://www.youtube.com/watch?v=gbRDCWKqvEc"],
    ["Top Gun", "The Top Gun Naval Fighter Weapons School", "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg", "https://www.youtube.com/watch?v=qAfbp3YX9F0"],

]
movie_objects = []

for movie in movie_data:
    movie_objects.append(media.Movie(movie[0], movie[1], movie[2], movie[3]))

fresh_tomatoes.open_movies_page(movie_objects)
