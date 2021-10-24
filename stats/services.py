import os 
from requests import Request, Session
from requests.sessions import session
from django.conf import settings
import json

def get_infoStats():
    info_stats = []
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug':'bitcoin',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'applications/json',
        'X-CMC_PRO_API_KEY': settings.OXFORD_APP_KEY
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price = format((data['data']['1']['quote']['USD']['price']), ".2f")
        percent_change_24h = format(abs((data['data']['1']['quote']['USD']['percent_change_24h'])),".2f")
        percent_change_7d = format(abs((data['data']['1']['quote']['USD']['percent_change_7d'])), ".2f")
        return price, percent_change_24h, percent_change_7d
    except:
        print('Somthing is wrong')


get_infoStats()