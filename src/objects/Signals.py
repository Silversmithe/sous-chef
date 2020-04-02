import threading


class Signals(object):

    def __init__(self):
        self.System_Running = True
        self.AudioEngineActive = True
        self.ListenerEngineActive = True