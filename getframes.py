import subprocess as sp
import numpy as np


FFMPEG_BIN = "ffmpeg"
MAIN_VID_DIR = 'Videos/'

def time_into_hash(time_str):
    return_str = ''
    for s in time_str:
        if s.isdigit():
            return_str += s
    return return_str

def get_frame(file_name, time_):
    file_name_with_dir = MAIN_VID_DIR + file_name
    file_name_with_dir_no_ending = MAIN_VID_DIR + file_name[:len(file_name) - 4]
    file_name_no_ending = file_name[:len(file_name) - 4]
    final_dir = MAIN_VID_DIR + file_name_no_ending + '/' + file_name
    print(final_dir)

    command = [ FFMPEG_BIN,'-n',
            '-i', final_dir,
            '-ss', time_,
            '-vframes', '1',
            final_dir + time_into_hash(time_) + '.' + 'png']

    pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
    pipe.stdout.flush()
    return final_dir + time_into_hash(time_) + '.' + 'png'