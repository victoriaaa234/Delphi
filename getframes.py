import subprocess as sp
import numpy as np

FFMPEG_BIN = "ffmpeg"


def time_into_hash(time_str):
    return_str = ''
    for s in time_str:
        if s.isdigit():
            return_str += s
    return return_str

def get_frame(file_name, time_):
    command = [ FFMPEG_BIN,
            '-i', TEST_VID_NAME,
            '-ss', TEST_VID_TIME,
            '-vframes', '1',
            file_name + time_into_hash(time_) + '.' + 'png']

    pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
    pipe.stdout.flush()
    return





