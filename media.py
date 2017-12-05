import webbrowser
class Movie():
    def __init__(self, m_title, m_story, m_poster, m_trailer):
        self.title = m_title
        self.story = m_story
        self.poster = m_poster
        self.trailer = m_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
        

