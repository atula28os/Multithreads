import os
import threading
from sqlalchemy import create_engine
from sqlalchemy import text
from datetime import datetime
from queue import Empty

class PostgresMasterScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(PostgresMasterScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
        
    def run(self):
        
        while True:
            try:
                val = self._input_queue.get(timeout=10)
            except Empty:
                print("Queue Timeout..")
                break
                
            if val == 'DONE':
                break
            
            symbol, price, extracted_time = list(val) 
            if price is None:
                price = 0.00
            extracted_time = str(datetime.strptime(extracted_time, "%Y-%m-%d %H:%M:%S"))
            postgres_worker = PostgresWorker(symbol=symbol, price=price, extracted_time=extracted_time)
            postgres_worker._insert_into_db()
    
class PostgresWorker():
    
    def __init__(self,symbol, price, extracted_time) -> None:
        self._symbol = symbol
        self._price = price
        self._extracted_time = extracted_time 
        # self._mysql_user = os.environ.get('MYSQL_USER')
        # self._mysql_pwd = os.environ.get('MYSQL_PASSWORD')
        # self._con_engine = create_engine(f'mysql+pymysql://{self._mysql_user}:{self._mysql_pwd}@{self._mysql_host}/{self._mysql_db}')
        # self._'NAME': 'django',
        # 'USER': 'root',
        # 'PASSWORD': 'Atul@14ocrores',
        # 'HOST': 'localhost', # Or an IP Address that your DB is hosted on
        # 'PORT': '3306'
        self._conn_string = 'mysql+pymysql://root:Atul%4014029@localhost/multi'
        self._engine = create_engine(self._conn_string)
        
    def _create_insert_query(self):
        query = text("INSERT INTO PRICES(symbol, price, extracted_time) VALUES (:symbol, :price, :extracted_time)")
        return query
    
    def _insert_into_db(self):
        
        insert_query = self._create_insert_query()
        
        with self._engine.connect() as conn:
            conn.execute(insert_query, {'symbol':self._symbol, 
                                        'price':self._price, 
                                        'extracted_time':self._extracted_time})
            
        
            conn.commit()