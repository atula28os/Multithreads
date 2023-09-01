import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


class WikiWorker():
    
    def __init__(self) -> None:
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        
    @staticmethod
    def _extract_company_symbol(page_html):
        soup = BeautifulSoup(page_html,'html.parser')
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')
        for table_row in table_rows[1:]:
            symbol = table_row.find('td').text.strip('\n')
            yield symbol
            
        
    def get_sp_500_companies(self):
        response = requests.get(url=self._url)
        if response.status_code != 200:
            logger.warning('Not able to find companies!')
            return []
        yield from self._extract_company_symbol(response.text)
        
        
if __name__ == '__main__':
    wiki = WikiWorker()
    counter = 0
    for symbol in wiki.get_sp_500_companies():
        print(symbol)
        counter += 1
        if counter > 5:
            break
        
        