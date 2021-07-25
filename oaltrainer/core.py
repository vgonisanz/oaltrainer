from openal import *

import time

class Core:
    def __init__(self):
        print('loading_openal')
        self._source = oalOpen("resources/ak-47_fire-01.wav")

    def run(self):
        self._source.play()
        while self._source.get_state() == AL_PLAYING:
	        time.sleep(1)

    # Deleting (Calling destructor)
    def __del__(self):
        print('unloading_openal')
        oalQuit()
