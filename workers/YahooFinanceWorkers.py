import threading
from typing import Any
import requests
import logging
import json 

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

class YahooFinancePriceWorker(threading.Thread):
    def __init__(self, symbol, *args, **kwargs):
        super(YahooFinancePriceWorker,self).__init__(*args, **kwargs)
        self._symbol = symbol
        api_keys = 'YRM6XZE300TP86DR'
        base_url = 'https://www.alphavantage.co/query'
        self._url = f'{base_url}?function=GLOBAL_QUOTE&symbol={self._symbol}&apikey={api_keys}'
        self._price = None
        self.start()
        
    def get_price(self):        
        try:
            response = requests.get(self._url)
            data = response.json()
            self._price = float(data['Global Quote']["05. price"])
            print(f"Price for {self._symbol}: {self._price}")
        except Exception as ex:
            logger.warning(f"Not able to find the price for {self._symbol}")

    def run(self):
        self.get_price()
    
    
    
        