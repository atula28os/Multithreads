import threading
import time 


class SleepersWorker(threading.Thread):
    def __init__(self, seconds, *args, **kwargs):
        super(SleepersWorker, self).__init__(*args, **kwargs)
        self._seconds = seconds
        self.start()
        
    def _let_me_sleep(self):
        print("Sleeping..")
        time.sleep(self._seconds)
        
    def run(self):
        self._let_me_sleep()
        
        