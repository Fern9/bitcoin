from apis.btcc.api import BtccAPI
from apis.huobi.api import HuobiAPI
from apis.okcoin.api import OkAPI

apikey = 'a'
secretkey = 'b'
api = BtccAPI(apikey, secretkey)
print api.ticker()

api = OkAPI(apikey, secretkey)
print api.ticker('btc_cny')

api = HuobiAPI(apikey, secretkey)
print api.ticker()


