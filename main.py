
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancePriceWorker

def main():    
    wiki_worker = WikiWorker()
    current_workers = []
    companies = {}
    counter = 0
    
    for symbol in wiki_worker.get_sp_500_companies():
        if counter < 10:
            counter += 1
            yahoo_finace_price_worker = YahooFinancePriceWorker(symbol=symbol)
            current_workers.append(yahoo_finace_price_worker)
            companies[symbol] = yahoo_finace_price_worker._price
        else:
            break
    
    for i, worker in enumerate(current_workers):
        worker.join()
    
    print(companies.items())

if __name__ == "__main__":
    main()