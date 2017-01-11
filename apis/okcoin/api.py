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
