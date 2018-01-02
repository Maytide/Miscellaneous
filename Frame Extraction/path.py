import os


with open('path.txt') as f:
    files = f.readlines()

readpath = files[0].strip('\n')
videos = [video.strip('\n') for video in files[1:]]
# print(len(videos))
writepath = 'frames\\'