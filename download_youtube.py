from pytube import YouTube
VID_DIR = '/Users/jusunglee/Work/TAMU/CSCE315/CSCE_315_TeamProject_3/Videos/'

def download_youtube_video(url):
    id_prec = 'watch?v='
    file_type = 'mp4'
    vid_quality = '720p'
    yt = YouTube(url)
    print('^^^^^^^$^%#$^#$&%$^&^*$*')
    print(yt.get_video_data())
    print('^^^^^^^$^%#$^#$&%$^&^*$*')
    yt_ID_index = url.find(id_prec)
    yt_ID = url[yt_ID_index + len(id_prec):]
    yt.set_filename(yt_ID)
    video = yt.get(file_type, vid_quality)
    video.download(VID_DIR)
    return yt_ID + '.' + file_type