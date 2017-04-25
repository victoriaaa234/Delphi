from pytube import YouTube
import moviepy.editor as mp
import os

VID_DIR = '/Users/jusunglee/Work/TAMU/CSCE315/CSCE_315_TeamProject_3/Videos/'
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
    if not os.path.exists(VID_DIR_X):
        os.makedirs(VID_DIR_X)
    video.download(VID_DIR_X)
    vid_path = MAIN_DIR + yt_ID + '/' + yt_ID + '.' + file_type
    print('%%%%%%%%')
    print(vid_path)
    duration =  mp.VideoFileClip(vid_path).duration
    print(int(duration))
    return yt_ID + '.' + file_type, duration