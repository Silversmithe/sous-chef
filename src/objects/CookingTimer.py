#
# CookingTimer.py
#
# This object serves as a container for a cooking timer.
#
import time


class CookingTimer(object):

    IDENTIFIER = 0

    def __init__(self, pneumonic, duration):
        self.__id = CookingTimer.IDENTIFIER
        CookingTimer.IDENTIFIER += 1
        self.pneumonic = pneumonic
        self.start_time = int(time.time())
        self.duration = duration
        self.end_time = self.start_time + self.duration
        self.is_active = True
