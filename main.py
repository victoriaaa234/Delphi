from download_youtube import download_youtube_video
from pool import ConsumerThread
from pool import ProducerThread
from clarify import process_image
from getframes import get_frame
import os
import time
import os.path
from pathlib import Path


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
    MAIN_DIR = 'Videos/'
    file_type = 'mp4'
    yt_id = url.rfind('=')
    yt_ID = url[yt_id+1:]
    vid_path = MAIN_DIR + yt_ID + '/' + "results.csv"
    vid_file = Path(vid_path)
    print(vid_path)
    if vid_file.is_file():
        print('Already downloaded! Skipping download and function calls.')
        log = open(MAIN_DIR + yt_ID + '/' + 'results.csv','r')
        i = 0
        results_list = []
        with log as f:
            for line in f:
                num = int(line[:line.find(',')])
                if search_term.lower() in line:
                    _index = line.index(search_term.lower())
                    line = line[_index:]
                    line = line[line.index(',')+1:]
                    print(line)
                    line = line[:line.index('"')]
                    results_list.append([num,line])
                i += 1
        return results_list
    else:
        file_name, seconds = download_youtube_video(url)
        image_list = []
        for second in range(int(seconds)):
            minutes = int(second / 60)
            hours = int(minutes / 60)
            hours_str = str(hours)
            minutes_str = str(minutes)
            seconds_str = str(second % 60)
            print(second % 60)
            if second % 60 < 10:
                print('uip')
                seconds_str = '0' + str(second % 60)
            if minutes < 10:
                minutes_str = '0' + str(minutes)
            if hours < 10:
                hours_str = '0' + str(hours)
            print('min ' + minutes_str)
            print('hour ' + hours_str)
            print('seconds ' + seconds_str)
            formatted_time = hours_str + ':' + minutes_str + ':' + seconds_str
            #print(formatted_time)
            image_path = get_frame(file_name,formatted_time)
            image_list.append(image_path)
        # time.sleep(5)

        results_list = []
        file_ = open(MAIN_DIR + yt_ID + '/' + 'results.csv','w+')
        i = 0
        for image in image_list:
            print(image)
            results = process_image(image)
            file_.write(str(i)+',')
            for result in results:
                file_.write('"' + str(result[0]) + ',' + str(result[1]) + '",')
            file_.write('\n')
            i += 1
            first_col = [x[0] for x in results]
            if search_term.lower() in first_col:
                index_ = first_col.index(search_term.lower())
                results_list.append(index_, results[index_][1])
        print('dONE')
        return results_list

#print(main('https://www.youtube.com/watch?v=QbmDpEhAp48', 'weapon'))

#https://www.youtube.com/watch?v=BfXSRQtilNw GUARDIANS OF THE GALAXY | WOMAN or FLAME
#https://www.youtube.com/watch?v=2BDyeARyIkw STAR WARS | WOMAN
#https://www.youtube.com/watch?v=9ec5XKAzKfk WONDER WOMAN
#https://www.youtube.com/watch?v=ql7uY36-LwA PUPPY MONKEY BABY
#https://www.youtube.com/watch?v=668nUCeBHyY city

#https://www.youtube.com/watch?v=eDd3yWEiNLY explosion | man
#https://www.youtube.com/watch?v=yN3kD1REAas monkey/
#https://www.youtube.com/watch?v=AIhJvXPZH6U iron man "explosion"