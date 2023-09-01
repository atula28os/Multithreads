from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any

class SumSquaredWorker(threading.Thread):

    def __init__(self,n, *args, **kwargs):
        super(SumSquaredWorker,self).__init__(*args, **kwargs)
        self._n = n
        self.start()
        
        
    def _calculate_sum_square(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2
        print("sum of squares: ", sum_squares)
        
    def run(self):
        self._calculate_sum_square()