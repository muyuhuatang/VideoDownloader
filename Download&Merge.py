# Prepare:
# should 'pip install moviepy' to merge files by moviepy package
# should 'pip install natsort' to sort files by natsort package
import sys
from urllib.error import HTTPError
from urllib.request import urlopen

## get all urls

with open('/Users/username/Downloads/URL.txt') as f:
    lines = f.readlines()

## download urls
print(lines[0])
print(len(lines))

try:
    for i in range(0, len(lines)):
        url = lines[i]
        print(url)
        filedata = urlopen(url)
        datatowrite = filedata.read()

        output = '/Users/username/Downloads/Temp/'+str(i)+'.ts'
        with open(output, 'wb') as f:
            f.write(datatowrite)
except HTTPError:
    print('HTTPError occurs, means there are less than 121 video slices')
except:
    print('Something else went wrong')

## merge videos
# use 'ulimit -n 1024' to set the open file limits of system on MAC, original is 256
from moviepy.editor import *
import os
from natsort import natsorted

L =[]
cwd = '/Users/username/Downloads/Temp/'
files = os.listdir(cwd)  
print("Files in %r: %s" % (cwd, files))

for root, dirs, files in os.walk(cwd):
    #files.sort()
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.ts':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)
            # remove temp file
            os.remove(filePath)

final_clip = concatenate_videoclips(L)
# how to apply API: https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html
final_clip.write_videofile("output.mp4", remove_temp=True)
