#!/bin/python
import os

# find out system
with open("/etc/os-release") as osRelease:
    if "ID=fedora" in map(lambda n: n.rstrip("\n"), osRelease.readlines()):
        opera = "/usr/lib64/opera"
    else:
        opera = "/usr/lib/x86_64-linux-gnu/opera"

# change to appropriate dir
os.chdir(opera)

# update ffmpeg
os.system("snap install chromium-ffmpeg")

# get newest version of ffmpeg
arr = []
for i in os.listdir("/snap/chromium-ffmpeg/current/"):
    if i.startswith("chromium"):
        arr.append(int(i.split("-")[-1]))

arr.sort()

# build ffmpeg location
ffmpeg="/snap/chromium-ffmpeg/current/chromium-ffmpeg-" + str(arr[-1]) + "/chromium-ffmpeg/libffmpeg.so"

# save original ffmpeg
os.rename("libffmpeg.so", "libffmpeg.so_original")

# make new symbolic link
os.system("sudo ln -sf " + ffmpeg + " libffmpeg.so")

print("\n\nLatest ffmpeg: " + ffmpeg)
print("done!")
