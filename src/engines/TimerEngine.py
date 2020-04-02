#
# TimerEngine.py
#

import threading
import time

from objects.CookingTimer import CookingTimer
from objects.Signals import Signals


class TimerEngine(threading.Thread):

    def __init__(self, signals, manager, manager_lock):
        threading.Thread.__init__(self)
        # interface data
        self.__signals = signals
        self.__manager = manager
        self.__manager_lock = manager_lock
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

            time.sleep(0.1)

        print('Timer Engine is Finished')