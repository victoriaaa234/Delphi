from download_youtube import download_youtube_video
from pool import ConsumerThread
from pool import ProducerThread
from clarify import process_image
from getframes import get_frame


TEST_IMAGE = 'test.png'
TEST_URL = 'https://www.youtube.com/watch?v=W6O009NoWDQ'
TEST_VID_NAME = 'W6O009NoWDQ.mp4'
TEST_VID_TIME = '00:00:03.435'

def test_clarifai():
    process_image(TEST_IMAGE)
    return

def test_youtube_downloader():
    print('Downloading Test Youtube Video')
    download_youtube_video(TEST_URL)
    print('Done!')
    return

def test_get_frame():
    print('Testing frame grabber')
    get_frame(TEST_VID_NAME, TEST_VID_TIME)
    return

def get_frames_of_youtube_video(url):
    yt_file_name, yt_duration = download_youtube_video(url)


    
    
# video = input('Enter youtube URL')
# query = input('Enter query term')
test_youtube_downloader()

