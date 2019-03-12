right now, the streamlink on youtube live support might be broken.
https://t.co/Qk93u6sCyr


# What is this?
Use Python to download YoutubeLiveVideo, FOREEVER!!!!!

I used this to construct a long duration video dataset for my research.

# How?
We also use apscheduler, so it will download the video every hour.

Python 3.5 or 3.6 required.

# What should I do?
change the url in the downloader.py to the video you want.

# Requirements? Usage?
you need apscheduler and streamlink:

```
git clone https://github.com/kentaroy47/youtube-stream-downloader.git
pip install apscheduler==2.1.2 # you need this version.
pip install streamlink
```

Then, run:

```
python downloader.py

```
