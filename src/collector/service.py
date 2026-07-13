from .validator import URLValidator
from .downloader import Downloader
from .exceptions import InvalidURLException


class CollectorService:

    def __init__(self):
        self.downloader = Downloader()

    def collect(self, url: str):

        if not URLValidator.is_valid(url):
            raise InvalidURLException("Invalid YouTube URL")

        return self.downloader.download(url)
Add collector service
