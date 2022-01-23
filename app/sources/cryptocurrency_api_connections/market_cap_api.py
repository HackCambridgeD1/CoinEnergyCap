from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from app.sources.cryptocurrency_data_schema import demo_cryptocurrency_metadata


def get_symbol_market_cap_map():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': ",".join(demo_cryptocurrency_metadata.demo_metadata_symbol)
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '73abeeec-fb99-459f-8da1-544e37f4ccf9',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = response.json()
        data = data["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        data = {}
        print(e)

    return {symbol: info["quote"]["USD"]["market_cap"] for symbol, info in data.items()}

