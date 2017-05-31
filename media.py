import webbrowser


class Movie:
    """A class that holds information for a movie.
    
    Attributes:
        title: The movie's title.
        storyline: A summary of the movie.
        poster_image_url: An URL pointing to the movie's poster image
        trailer_youtube_url: An Youtube link to the movie trailer.
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Opens a browser and navigates to the youtube trailer."""
        webbrowser.open(self.trailer_youtube_url)
