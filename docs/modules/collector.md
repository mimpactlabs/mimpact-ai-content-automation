# Collector Module

## Purpose

Download content from supported sources and save it locally.

---

## Responsibilities

- Validate source URL
- Download video
- Save video
- Create metadata

---

## Does NOT

- Speech to text
- AI analysis
- Subtitle generation
- Clip generation
- Upload

---

## Input

YouTube URL

Example

https://www.youtube.com/watch?v=XXXXXXXX

---

## Output

Video

data/downloads/{video_id}.mp4

Metadata

data/downloads/{video_id}.json

---

## Metadata Example

{
    "id": "",
    "title": "",
    "channel": "",
    "duration": 0,
    "url": "",
    "downloaded_at": "",
    "video_file": ""
}
