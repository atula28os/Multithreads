
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancePriceScheduler
from workers.PostgresWorker import PostgresMasterScheduler
from multiprocessing import Queue


def main():    
    symbol_queue = Queue()
    mysql_queue = Queue()
    wiki_worker = WikiWorker()
    
    yahoo_finance_threads = []
    mysqldb_threads = []
    counter = 0
    num_workers = 4
    
    for i in range(num_workers):
        yahoo_finance_price_scheduler = YahooFinancePriceScheduler(input_queue=symbol_queue, output_queue=mysql_queue)
        yahoo_finance_threads.append(yahoo_finance_price_scheduler)
        
        mysql_thread_scheduler = PostgresMasterScheduler(input_queue=mysql_queue)
        mysqldb_threads.append(mysql_thread_scheduler)
    
    for symbol in wiki_worker.get_sp_500_companies():
        if counter < 10:
            counter += 1
            symbol_queue.put(symbol)
    
    symbol_queue.put("DONE")
    
    for i, worker in enumerate(yahoo_finance_threads):
        worker.join()
    
    for j, worker in enumerate(mysqldb_threads):
        worker.join()
        
    
if __name__ == "__main__":
    main()