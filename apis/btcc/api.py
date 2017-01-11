from apis.btcc.rest import BaseHTTPs


class BtccAPI(BaseHTTPs):
    def __init__(self, apikey, secretkey):
        self.apikey = apikey
        self.secretkey = secretkey
        self.RESTURL = 'https://data.btcchina.com'

    def ticker(self, symbol='btccny'):
        url = "%s/data/ticker?market=%s" % (self.RESTURL, symbol)
        return self.get(url)
