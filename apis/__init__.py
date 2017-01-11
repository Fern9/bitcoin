from apis.btcc.api import BtccAPI
from apis.huobi.api import HuobiAPI
from apis.okcoin.api import OkAPI
from apis.settings import apikey, secretkey

btcc_api = BtccAPI(apikey, secretkey)

ok_api = OkAPI(apikey, secretkey)

huobi_api = HuobiAPI(apikey, secretkey)


