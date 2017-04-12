from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp


NUM_THRESHOLD = 20 # Numeric threshold for how many results to include.
PROB_THRESHOLD = 0.8 # Probabilistic threshold for lower limit of confidence rate of image
TEST_IMAGE = 'test.png'

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

process_image(TEST_IMAGE)