#
# TimerEngine.py
#

import threading
import time

from objects.CookingTimer import CookingTimer
from objects.Signals import Signals


class TimerEngine(threading.Thread):

    def __init__(self, signals, timer_manager, phrases):
        threading.Thread.__init__(self)
        # interface data
        self.__signals_lock = signals[0]
        self.__signals = signals[1]

        self.__manager_lock = timer_manager[0]
        self.__manager = timer_manager[1]

        self.__phrases_lock = phrases[0]
        self.__phrases = phrases[1]

        # state data
        self.__current_time = None

    def run(self):
        while self.__signals.System_Running == True:

            self.__current_time = int(time.time())

            with self.__manager_lock:
                for timer in self.__manager.getTimers():
                    if timer.end_time < self.__current_time and timer.is_active == True:
                        print('{} timer completed!'.format(timer.pneumonic))
                        timer.is_active = False
                        with self.__phrases_lock:
                            self.__phrases.append("{} timer completed!".format(timer.pneumonic))

            time.sleep(0.1)

        print('Timer Engine is Finished')