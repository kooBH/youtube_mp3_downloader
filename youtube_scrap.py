from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
    elif d['status'] == 'downloading' :
        print("Downloading : " + str(round( (d['downloaded_bytes'] / d['total_bytes'] )* 100 , 2) ) + "%")


ydl_opts = {
    'format': 'bestaudio/best',
     #파일이름 default %(title)s-%(id)s.%(ext)s
     #'outtmpl':'%(title)s.',
    'outtmpl':'%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',

    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['https://youtu.be/WfwnietuaME'])
  #ydl.download(['https://youtu.be/MAdQyx88k7E'])
'''

1. ffprobe 를 받아야함
https://ffmpeg.org/download.html
압축풀고 bin 폴더 환경변수 설정

ffmpeg
O:\Libraries\ffmpeg\bin\ffprobe.exe;O:\Libraries\ffmpeg\bin\ffplay.exe;O:\Libraries\ffmpeg\bin\ffmpeg.exe;
path  %ffmpeg%;
-> 잘 못받네

그냥 conda install ffmpeg 함

'''
