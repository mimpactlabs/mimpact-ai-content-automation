from yt_dlp import YoutubeDL


class Downloader:

    def download(self, url: str, output_path: str = "data/downloads"):

        options = {
            "outtmpl": f"{output_path}/%(id)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        }

        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            return info
Add YouTube downloader
