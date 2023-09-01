from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any
import requests
import logging
import json 

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(YahooFinancePriceScheduler,self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
        
    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break 
            
            yahoo_finance_price_worker = YahooFinancePriceWorker(symbol=val)
            price = yahoo_finance_price_worker.get_price()
            # self._output_queue.put(json.dumps({'symbol': val, 'price': price}))
            print(price)


class YahooFinancePriceWorker():
    def __init__(self, symbol, *args, **kwargs):
        super(YahooFinancePriceWorker,self).__init__(*args, **kwargs)
        self._symbol = symbol
        api_keys = 'YRM6XZE300TP86DR'
        base_url = 'https://www.alphavantage.co/query'
        self._url = f'{base_url}?function=GLOBAL_QUOTE&symbol={self._symbol}&apikey={api_keys}'
        self._price = None
        
    def get_price(self):        
        try:
            response = requests.get(self._url)
            data = response.json()
            self._price = float(data['Global Quote']["05. price"])
            print(f"Price for {self._symbol}: {self._price}")
            return self._price
        except Exception as ex:
            logger.warning(f"Not able to find the price for {self._symbol}")
    
    
        