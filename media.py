import webbrowser


class Movie():
    """class Movie is class to create instances of movies, which has four
    attributes: title, story, poster, trailer"""
    def __init__(self, m_title, m_story, m_poster, m_trailer):
        self.title = m_title
        self.story = m_story
        self.poster = m_poster
        self.trailer = m_trailer

    def show_trailer(self):
        """This function opens the web browser and opens the trailer for
        the given movie instance"""
        webbrowser.open(self.trailer)
