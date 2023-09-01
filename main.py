
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancePriceScheduler

from multiprocessing import Queue


def main():    
    symbol_queue = Queue()
    wiki_worker = WikiWorker()
    
    yahoo_finance_threads = []
    counter = 0
    
    yahoo_finance_price_scheduler = YahooFinancePriceScheduler(input_queue=symbol_queue)
    yahoo_finance_threads.append(yahoo_finance_price_scheduler)
    
    for symbol in wiki_worker.get_sp_500_companies():
        if counter < 10:
            counter += 1
            symbol_queue.put(symbol)
    
    symbol_queue.put("DONE")
    
    for i, worker in enumerate(yahoo_finance_threads):
        worker.join()
        
        
if __name__ == "__main__":
    main()