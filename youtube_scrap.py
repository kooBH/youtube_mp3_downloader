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
        if 'total_bytes' in d:
            print("Downloading : " + str(round( (d['downloaded_bytes'] / d['total_bytes'] )* 100 , 2) ) + "%")
        else:
             #이 URL의 경우 total_bytes를 못 받음 https://youtu.be/yjsfB4zJ4Is
             print("Downloading : But couldn't get total_bytes")


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

with open('lists.txt') as f:
    lines = f.readlines()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         ydl.download(lines)
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
