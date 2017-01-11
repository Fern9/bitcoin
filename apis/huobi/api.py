from apis.huobi.rest import BaseHTTPs


class HuobiAPI(BaseHTTPs):
    def __init__(self, apikey, secretkey):
        self.apikey = apikey
        self.secretkey = secretkey
        self.RESTURL = 'https://api.huobi.com/apiv3'

    def ticker(self, symbol=None):
        url = "http://api.huobi.com/staticmarket/ticker_btc_json.js"
        return self.get(url)
