from apis.okcoin.rest import BaseHTTPs


class OkAPI(BaseHTTPs):
    def __init__(self, apikey, secretkey):
        self.apikey = apikey
        self.secretkey = secretkey
        self.RESTURL = 'https://www.okcoin.cn'

    def ticker(self, symbol='btc_cny'):
        url = "%s/api/v1/ticker.do" % self.RESTURL
        params = None
        if symbol:
            params = {
                symbol: symbol
            }
        return self.get(url, params)

    def kline(self, symbol='btc_cny', type='1min', size=None, since=None):
        url = "%s/api/v1/kline.do" % self.RESTURL
        params = {}
        if symbol:
            params['symbol'] = symbol
        if type:
            params['type'] = type
        if size:
            params['size'] = size
        if since:
            params['since'] = since
        return self.get(url, params)
