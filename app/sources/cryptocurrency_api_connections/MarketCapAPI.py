from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from sources.cryptocurrency_data_schema import demo_cryptocurrency_metadata


def get_symbol_market_cap():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories'
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
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        data = {}
        print(e)

    market_cap = []
    for cryptocoin in data.get('data'):
        market_cap += [cryptocoin.get('market_cap')]

    crypto_market_cap = list(zip(demo_cryptocurrency_metadata.demo_metadata_symbol, market_cap))
    return {symbol: market_cap for symbol, market_cap in crypto_market_cap}
