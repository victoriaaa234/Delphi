from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
from pytube import YouTube

NUM_THRESHOLD = 20 # Numeric threshold for how many results to include.
PROB_THRESHOLD = 0.8 # Probabilistic threshold for lower limit of confidence rate of image
TEST_IMAGE = 'test.png'
VID_DIR = '/Users/jusunglee/Work/TAMU/CSCE315/CSCE_315_TeamProject_3/Videos/'


def setup_model(): # constructs boiler plate to get model ready
    f = open('TOKENS','r')
    lines = f.readlines()
    f.close()
    CLIENT_ID = lines[0][:-1]
    CLIENT_SECRET = lines[1]
    app = ClarifaiApp(CLIENT_ID, CLIENT_SECRET)
    ACCESS_TOKEN = app.auth.get_token()
    model = app.models.get('general-v1.3')
    return model

def process_image(filename):
    model = setup_model()
    image = ClImage(file_obj=open(filename, 'rb'))
    json_dict = model.predict([image])
    results = json_dict['outputs'][0]['data']['concepts']
    for i in range(0,NUM_THRESHOLD):
        name = results[i]['name']
        value = results[i]['value']
        if value < PROB_THRESHOLD:
            break
        else:
            print(name + ' : ' + str(value))
    return

def downloadYoutubeVideo(url):
    id_prec = 'watch?v='
    file_type = 'mp4'
    vid_quality = '720p'
    yt = YouTube(url)
    yt_ID_index = url.find(id_prec)
    yt_ID = url[yt_ID_index + len(id_prec):]
    yt.set_filename = yt_ID
    video = yt.get(file_type, vid_quality)
    video.download(VID_DIR)
    return

TEST_URL = 'https://www.youtube.com/watch?v=W6O009NoWDQ'
downloadYoutubeVideo(TEST_URL)
print('Done!')