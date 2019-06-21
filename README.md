# youtube_mp3_downloader
Download audio of a youtube video as mp3 file using youtube-dl library

# Dependency 
+ [Youtube-DL](https://rg3.github.io/youtube-dl/)  
**Windows PowerShell**
```
pip install --upgrade youtube_dl
```
+ [ffmpeg](https://www.ffmpeg.org/) -- 없어도 mp3 받는데는 문제가 없다 -- 
1. **Windows PowerShell**
```
pip install ffmpeg
```
2. Download ffmpeg unzip.
3. Add its 'bin' folder to System PATH 

## Usage
This Python script reads url from lists.txt which contains address of Youtube video.
And download its audio as mp3 file

