# Program to download files on flight

from pytube import YouTube
from sys import argv

link=argv[1]
yt=YouTube(link)
print("Title: ", yt.title)
print("Views:", yt.views)
yt=yt.streams.get_highest_resolution
yt.download('/Users/Khushi/Desktop')

print("download complete")
