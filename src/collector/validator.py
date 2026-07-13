from urllib.parse import urlparse


class URLValidator:
    SUPPORTED_DOMAINS = (
        "youtube.com",
        "www.youtube.com",
        "youtu.be",
    )

    @staticmethod
    def is_valid(url: str) -> bool:
        try:
            parsed = urlparse(url)
            return parsed.netloc in URLValidator.SUPPORTED_DOMAINS
        except Exception:
            return False
Add YouTube URL validator
