

class Movie:
    """The Movie class accepts a movie title, storyline, poster_image_url and trailer_youtube_url as arguments
    to create a new Movie object."""
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
