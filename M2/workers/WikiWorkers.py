import sys
import requests
import json 

sys.path.append('../')

from config import FMP

# API ENDPOINT & KEY
TICKER_URL = FMP.TICKER_URL
CASHFLOW_URL = FMP.CASHFLOW_URL
API_KEY = FMP.API_KEY

class WikiWorker():
    
    def __init__(self, url, cashflow_url) -> None:
        self._url = url 
        self._cashflow_url = cashflow_url
        
    def get_companies_symbol(self, query, count=None):
        self.query = query
        self.response = requests.get(url=self._url, params={'query': query, 'limit': count, 'apikey': API_KEY}) 
        if self.response.status_code != requests.codes.OK:
            return []
        else:
            response_data = json.loads(self.response.text)
            for company in json.loads(self.response.text):
                yield company
                
    def get_company_data(self, symbol):
        
        if self.query is None:
            print("First, get the company symbol")
        else:
            self._symbol = symbol
        self.company_data = requests.get(url=f'{self._cashflow_url}/{self._symbol}', params={'apikey': API_KEY})
        return self.company_data.text
    
if __name__ == '__main__':
    
    wiki = WikiWorker(url=TICKER_URL, cashflow_url=CASHFLOW_URL)
    response = wiki.get_companies_symbol(query='AA',count=5)
    for item in response:
        symbol = item['symbol']
        company_data = wiki.get_company_data(symbol=symbol)
        if len(company_data) > 5:
            print(company_data)
            print('========================')