from objects.CookingTimer import CookingTimer


class CookingTimerManager(object):

    def __init__(self):
        self.__timers = list()

    def getTimers(self):
        return self.__timers

    def addTimer(self, pneumonic, duration):
        timer = CookingTimer(pneumonic, duration)
        self.__timers.append(timer)
        print('{} timer added for {} seconds'.format(pneumonic, duration))

    