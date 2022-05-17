# What is this?
Use Python to download YoutubeLiveVideos.

I used this to construct a long duration video dataset for my research.

# How?
`simple_download.py`: Just download a youtube video.

`download.py`: We use `Apscheduler` to download the video every hour.

Python >= 3.5 required.

# Requirements
you need apscheduler and streamlink:

```
git clone https://github.com/kentaroy47/youtube-stream-downloader.git
pip install apscheduler
pip install streamlink==3.2.0
```

# Usage 

Set video URL in `download.py`
```download.py
### CHANGE THE URL HERE ####
URL = 'https://www.youtube.com/watch?v=1EiC9bvVGnk'
```

Then, run:

```
python downloader.py

```
