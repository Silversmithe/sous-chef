import time
import threading

from objects.Signals import Signals

from managers.CookingTimerManager import CookingTimerManager

from engines.TimerEngine import TimerEngine

if __name__ == '__main__':

    signals = Signals()
    signals_lock = threading.Lock()

    timer_manager = CookingTimerManager()
    timer_manager_lock = threading.Lock()

    timer = TimerEngine(signals=signals, manager=timer_manager, manager_lock=timer_manager_lock)
    timer.start()

    time.sleep(5)

    with timer_manager_lock:
        timer_manager.addTimer('potato', 60)

    time.sleep(5)

    with timer_manager_lock:
        timer_manager.addTimer('broccoli', 120)

    time.sleep(5)

    with timer_manager_lock:
        timer_manager.addTimer('boiling water', 180)

    time.sleep(300)


    with signals_lock:
        signals.System_Running = False

    timer.join()