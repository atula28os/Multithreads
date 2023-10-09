import os
import sys
import pytest
import requests
from requests import codes
import json
import logging
from logging import basicConfig

M2_DIR_PATH = os.path.abspath(os.path.join(os.getcwd(), 'M2'))
sys.path.append(M2_DIR_PATH)

from config import FMP

TICKER_URL = FMP.TICKER_URL
API_KEY = FMP.API_KEY

logging.basicConfig(filemode='a')

logger = logging.getLogger('COMPANIES')

@pytest.fixture
def limit():
    return 5

@pytest.fixture
def name():
    return 'AA'

@pytest.fixture
def url():
    return f'{TICKER_URL}?apikey={API_KEY}'

def test_get_companies(url, name, limit):
    payload = {'query': name, 'limit': limit}
    response = requests.get(url, params=payload)
    assert response.status_code == codes.OK
    assert len(json.loads(response.text))== limit
    logger.info('LIMIT is Equal to LENGTH of Response: PASSES')