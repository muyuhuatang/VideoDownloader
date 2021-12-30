# VideoDownloader
Local apply of online video downloader

## Background
When find that many websites are hard to crawl the video mannually, and some websites even split the videoa into many small segements to avoid easy crawlling, then I write the python based download and merge code to support the video crawl works.

## Prerequisite
python package: moviepy / natsort

## Implementation Environment
MacBook Pro 2018 15'

## Implementation
### 1. Get the download urls for specific video
I find one site from google search and list here just for reference:
https://weibomiaopai.com/download-video-parser.php

* It is not hard to find the similar online services
* If you are conducting the works on the business or academic use, please double confirm if the apporaches are allowed 
* Please feel free to rerun or make tests on the codes but remember to aovid any illegal usage.

### 2. Put the urls in the URL.txt file and seperate urls by lines
also remember to confirm the cwd and other directories in the Download&Merge.py file.

### 3. Run the python codes
```
python Download&Merge.py
```

Get the final MP4 output video file.

## Reference
1. moviepy API: https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html
if you want to make more settings on the output video file, please check the function write_videofile() for more details in the website.
