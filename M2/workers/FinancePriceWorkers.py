import sys
import threading
import requests
import json 

sys.path.append('../')

from config import FMP

# API ENDPOINT & KEY
TICKER_URL = FMP.TICKER_URL
CASHFLOW_URL = FMP.CASHFLOW_URL
API_KEY = FMP.API_KEY

class FinancePriceWorker(threading.Thread):
    def __init__(self, symbol, *args, **kwargs):
        super(FinancePriceWorker, self).__init__()
        self._symbol = symbol
        self.start()
        
    def run(self):
        self.company_data = requests.get(url=f'{CASHFLOW_URL}/{self._symbol}', params={'apikey': API_KEY})
        data = self.company_data.text
        print('Data: ', data)
        return data