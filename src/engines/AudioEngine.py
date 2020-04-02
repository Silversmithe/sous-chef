#
# AudioEngine.py
#

import threading
import time

from gtts import gTTS
import os


class AudioEngine(threading.Thread):

    def __init__(self, signals, phrases):
        threading.Thread.__init__(self)
        self.__signals_lock = signals[0]
        self.__signals = signals[1]

        self.__phrases_lock = phrases[0]
        self.__phrases = phrases[1]

        self.__temp_output_file = 'temp.mp3'
        self.__tts_output = None

    def run(self):
        while self.__signals.System_Running == True:

            if self.__signals.AudioEngineActive == True:
                with self.__phrases_lock:
                    if len(self.__phrases) > 0:
                        phrase = self.__phrases.pop(0)
                        self.__tts_output = gTTS(phrase, 'en')
                        self.__tts_output.save(self.__temp_output_file)
                        os.system('mpg123 -q ' + self.__temp_output_file)
                        time.sleep(1)
        
            time.sleep(0.5)

        print('Audio Engine is Finished')