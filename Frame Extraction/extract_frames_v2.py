import os
from subprocess import call
from path import videos, readpath, writepath

# https://stackoverflow.com/questions/28806816/use-ffmpeg-to-resize-image
# ffmpeg -i input.jpg -vf scale=320:240 output_320x240.png

# https://stackoverflow.com/questions/38253406/extract-list-of-specific-frames-using-ffmpeg
# ffmpeg -i in.mp4 -vf select='eq(n\,100)+eq(n\,184)+eq(n\,213)' -vsync 0 frames%d.jpg

# ffmpeg -i "D:\Downloads\[VCB-Studio] Hibike! Euphonium 2 [1080p]\[VCB-Studio] Hibike! Euphonium 2 [01][1080p][x265_aac].mp4"
# -vf select='eq(n\,100)+eq(n\,184)+eq(n\,213)' -vsync 0 frames%d.jpg

# https://youtu.be/bVkYNJ2JSqM?t=3s
# approximate start frame for ep 1 (~2 mins in): 2500
for video in videos:
    readfile = os.path.join(readpath, video)
    call(["ffmpeg", "-i", readfile,
          "-vf", "select='eq(n\,1000)+eq(n\,1804)+eq(n\,2130)', scale=640:360", # Separate multiple vf with commas
          "-vsync", "0",
          os.path.join(writepath, "frames_"+video+"_%d.jpg")])

    break

