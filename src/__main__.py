import time
import threading

from objects.Signals import Signals

from managers.CookingTimerManager import CookingTimerManager

from engines.TimerEngine import TimerEngine
from engines.AudioEngine import AudioEngine

if __name__ == '__main__':

    signals = (threading.Lock(), Signals())
    timer_manager = (threading.Lock(), CookingTimerManager())
    phrases = (threading.Lock(), [])

    audio_engine = AudioEngine(signals=signals, phrases=phrases)
    timer_engine = TimerEngine(signals=signals, timer_manager=timer_manager, phrases=phrases)

    audio_engine.start()
    timer_engine.start()

    time.sleep(5)

    with timer_manager[0]:
        timer_manager[1].addTimer('potato', 5)

    time.sleep(5)

    with timer_manager[0]:
        timer_manager[1].addTimer('broccoli', 10)

    time.sleep(5)

    with timer_manager[0]:
        timer_manager[1].addTimer('boiling water', 15)

    time.sleep(100)

    with timer_manager[0]:
        timer_manager[1].System_Running = False

    timer_engine.join()
    audio_engine.join()
