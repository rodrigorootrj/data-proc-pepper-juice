import sys
sys.path.append("..")
import json
from lib.config import *
from requests import Session


class Preco:
    def preco(symbol):   
#        logging.INFO('STARTING preco')
        url = ds_url
        parameters = {
        'symbol' : symbol
        }
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': token_key,
        }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            valor = float(data['data'][symbol][0]['quote']['USD']['price'])
            if valor > 1:
                valor = '{:.2f}'.format(valor)
            elif valor < 1 and valor > 0.0001:
                valor = '{:.4f}'.format(valor)
            elif valor < 0.0001 and valor > 0.000001:
                valor = '{:.9f}'.format(valor)             
        except Exception as error:
            valor = 'error'
        return valor