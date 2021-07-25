from openal import *

import time

class FixedPositions:
    CENTER = [0, 0, 0]

class FixedOrientations:
    FRONT = [0, 0, 0]

class FixedVelocities:
    STOPPED = [0, 0, 0]

class Core:
    def __init__(self):
        print('loading_openal')
        self._initialize_listener()
        self._initialize_source()

    def run(self, sound_file):
        self._source.set_buffer(sound_file)
        self._source.play()
        while self._source.get_state() == AL_PLAYING:
	        time.sleep(1)

    def __del__(self):
        print('unloading_openal')
        oalQuit()
    
    def _initialize_listener(self):
        self._listener = openal.oalGetListener()
        self._listener.set_position(FixedPositions.CENTER)
        self._listener.set_orientation(FixedOrientations.FRONT)
        self._listener.set_velocity(FixedVelocities.STOPPED)
        self._listener.set_gain(1.0)
    
    def _initialize_source(self):
        self._source = oalOpen()
        self._source.set_pitch(1.0)
        self._source.set_gain(1.0)
        self._source.set_max_distance(1.0)
        self._source.set_rolloff_factor(1.0)
        self._source.set_position(FixedPositions.CENTER)
        self._source.set_velocity(FixedVelocities.STOPPED)
        self._source.set_looping(False)
