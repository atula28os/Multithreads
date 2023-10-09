import sys
import time 
from time import perf_counter

from workers.WikiWorkers import WikiWorker
from workers.FinancePriceWorkers import FinancePriceWorker

sys.path.append('../')

from config import FMP

# API ENDPOINT & KEY
TICKER_URL = FMP.TICKER_URL
CASHFLOW_URL = FMP.CASHFLOW_URL

# CODE STARTS
keywords = ['AA', 'PL', 'BN']

finance_workers_list = []

def main():
    for word in keywords:
        wiki = WikiWorker(url=TICKER_URL, cashflow_url=CASHFLOW_URL)
        companies_list_per_word = wiki.get_companies_symbol(query=word, count=5)
        for comp_symbol in companies_list_per_word:
            print('comp_symbol: ', comp_symbol,' <> ','word: ', word)
            financePriceWorker = FinancePriceWorker(symbol=comp_symbol['symbol'])
            finance_workers_list.append(financePriceWorker)

    for worker in finance_workers_list:
        worker.join()

# CODE ENDS
    
if __name__ == '__main__':
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f'TOTAL TIME FOR PROCESSING:  {end_time-start_time}')