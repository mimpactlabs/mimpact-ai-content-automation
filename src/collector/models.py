from dataclasses import dataclass


@dataclass
class VideoMetadata:
    id: str
    title: str
    channel: str
    duration: int
    url: str
    downloaded_at: str
    file_path: str
Add video metadata model
