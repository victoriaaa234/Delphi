from download_youtube import download_youtube_video
from pool import ConsumerThread
from pool import ProducerThread
from clarify import process_image
from getframes import get_frame
import os
import time

TEST_IMAGE = 'test.png'
TEST_URL = 'https://www.youtube.com/watch?v=W6O009NoWDQ'
TEST_VID_NAME = 'W6O009NoWDQ.mp4'
TEST_VID_TIME = '00:00:03.435'
FPS_FACTOR = 1 # FPS_FACTOR frames per second to send to clarifai

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

def main(url, search_term):
    file_name, seconds = download_youtube_video(url)
    image_list = []
    for second in range(int(seconds)):
        minutes = int(second / 60)
        hours = int(minutes / 60)
        hours_str = ''
        minutes_str = ''
        seconds_str = str(second % 60)
        if seconds % 60 < 10:
            seconds_str = '0' + seconds_str
        if minutes < 10:
            minutes_str = '0' + str(minutes)
        if hours < 10:
            hours_str = '0' + str(hours)
        formatted_time = hours_str + ':' + minutes_str + ':' + seconds_str
        #print(formatted_time)
        image_path = get_frame(file_name,formatted_time)
        image_list.append(image_path)
    # time.sleep(5)
    results_list = []
    for image in image_list:
        print(image)
        results = process_image(image)
        results_list.append(results)
        if search_term.lower() in results:
            index_ = image.rfind('.mp4')
            duration = image[index_ + 4:]
            duration = image[:image.rfind('.png')]
            print('Found ' + search_term.lower() + ' at duration: ' + duration)
    print('dONE')
    return_list = [range(int(seconds), results_list, image_list)]
    return return_list

main('https://www.youtube.com/watch?v=668nUCeBHyY', 'Flame')

#https://www.youtube.com/watch?v=BfXSRQtilNw GUARDIANS OF THE GALAXY | WOMAN or FLAME
#https://www.youtube.com/watch?v=2BDyeARyIkw STAR WARS | WOMAN
#https://www.youtube.com/watch?v=9ec5XKAzKfk WONDER WOMAN
#https://www.youtube.com/watch?v=ql7uY36-LwA PUPPY MONKEY BABY
#https://www.youtube.com/watch?v=668nUCeBHyY nature