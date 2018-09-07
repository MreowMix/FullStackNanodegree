import webbrowser


class Movie():
    # __doc__
    """This class provides a way to store movie related information"""

    # This is the class constructor that initilizes instance variables
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This instance method opens the youtube link
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
