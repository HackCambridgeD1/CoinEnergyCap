import logging
import time

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from app.sources.cryptocurrency_data_schema.demo_cryptocurrency_metadata import demo_metadata_symbol


def get_symbol_market_cap_map(symbol_list=demo_metadata_symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': ",".join(symbol_list)
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '73abeeec-fb99-459f-8da1-544e37f4ccf9',
    }

    session = Session()
    session.headers.update(headers)

    max_tries = 3
    current_try = 0
    current_delay = 1

    while current_try < max_tries:
        try:
            response = session.get(url, params=parameters)
            data = response.json()
            data = data["data"]
            break
        except Exception as e:
            time.sleep(current_delay)
            current_try += 1
            current_delay *= 2

            if current_try == max_tries:
                logging.error("Connecting to the coinmarketcap API failed multiple times in a row. "
                              "Please Try again later!")

    return {symbol: info["quote"]["USD"]["market_cap"] for symbol, info in data.items()}
