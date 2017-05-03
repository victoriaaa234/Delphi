from pytube import YouTube
import moviepy.editor as mp
import os
import os.path
from pathlib import Path
VID_DIR = 'usr/app/Videos/'
MAIN_DIR = 'Videos/'


def download_youtube_video(url):
    id_prec = 'watch?v='
    file_type = 'mp4'
    vid_quality = '720p'
    yt = YouTube(url)
    yt.get_video_data()
    yt_ID_index = url.find(id_prec)
    yt_ID = url[yt_ID_index + len(id_prec):]
    yt.set_filename(yt_ID)
    video = yt.get(file_type, vid_quality)
    VID_DIR_X = VID_DIR + yt_ID
    vid_path = MAIN_DIR + yt_ID + '/' + yt_ID + '.' + file_type
    vid_file = Path(vid_path)
    if vid_file.is_file():
        print('Already downloaded! Skipping download.')
        duration =  mp.VideoFileClip(vid_path).duration
        return yt_ID + '.' + file_type, duration
    if not os.path.exists(VID_DIR_X):
        os.makedirs(VID_DIR_X)
    try:
        os.remove(vid_path)
    except OSError:
        pass
    video.download(VID_DIR_X)

    print('%%%%%%%%')
    print(vid_path)
    duration =  mp.VideoFileClip(vid_path).duration
    print(int(duration))
    return yt_ID + '.' + file_type, duration
