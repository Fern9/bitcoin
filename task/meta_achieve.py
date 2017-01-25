import sys, json

sys.path.append('..')
import env
from time import sleep
from datetime import datetime
import time
from task.request import ConcurrentRequest
from apis import ok_api, huobi_api
from charts.models import OKCoinSpot, HuobiSpot, Config
from task.schedule import schedule
from apis.ws import WS
from huobi_client import StreamingClient


class OK_ws(WS):
    def on_open(self, ws):
        self.send({'event': 'addChannel', 'channel': 'ok_btccny_ticker'})
    def on_message(self, ws, data):
        print '#ok message#'
        message = data[0]
        if 'data' in message:
            ok_datas = {
                'date_stamp': float(message['data']['timestamp']),
                'date_time': datetime.fromtimestamp(float(message['data']['timestamp'])/1000.0),
                'buy': message['data']['buy'],
                'high': message['data']['high'],
                'last': message['data']['last'],
                'low': message['data']['low'],
                'sell': message['data']['sell'],
                'vol': message['data']['vol'],
                'symbol': 'btccny'
            }
            okcoin = OKCoinSpot(**ok_datas)
            # okcoin.save()

def get_okcoin_from_ws():
    ws = OK_ws('wss://real.okcoin.cn:10440/websocket/okcoinapi')
    # ws.on_open = on_okcoin_open
    ws.asyc_start()




def get_huobi_from_ws():
    def _on_huobi_message(data):
        print '#huobi message#'
        if 'payload' in data:
            data = data['payload']
            timestamp = time.time()
            huobi_datas = {
                'date_stamp': timestamp,
                'date_time': datetime.fromtimestamp(timestamp),
                'buy': data['priceBid'],
                'high': data['priceHigh'],
                'last': data['priceNew'],
                'low': data['priceLow'],
                'sell': data['priceAsk'],
                'vol': data['totalAmount'],
                'symbol': 'btccny'
            }
            huobi = HuobiSpot(**huobi_datas)
            # huobi.save()
        print data

    sclient = StreamingClient()
    sclient.subscribe('marketOverview')
    sclient.connect(_on_huobi_message)


def get_market():
    creq = ConcurrentRequest()

    creq.add(ok_api.ticker)
    creq.add(huobi_api.ticker)

    ok_res, huobi_res = creq.start()
    if ok_res and huobi_res:
        ok_datas = {
            'date_stamp': float(ok_res['date']),
            'date_time': datetime.fromtimestamp(float(ok_res['date'])),
            'buy': ok_res['ticker']['buy'],
            'high': ok_res['ticker']['high'],
            'last': ok_res['ticker']['last'],
            'low': ok_res['ticker']['low'],
            'sell': ok_res['ticker']['sell'],
            'vol': ok_res['ticker']['vol'],
            'symbol': 'btccny'
        }

        okcoin = OKCoinSpot(**ok_datas)
        okcoin.save()

        huobi_datas = {
            'date_stamp': float(huobi_res['time']),
            'date_time': datetime.fromtimestamp(float(huobi_res['time'])),
            'buy': huobi_res['ticker']['buy'],
            'high': huobi_res['ticker']['high'],
            'last': huobi_res['ticker']['last'],
            'low': huobi_res['ticker']['low'],
            'sell': huobi_res['ticker']['sell'],
            'vol': huobi_res['ticker']['vol'],
            'open': huobi_res['ticker']['open'],
            'symbol': 'btccny'
        }
        huobi = HuobiSpot(**huobi_datas)
        # huobi.save()


if __name__ == '__main__':

    get_okcoin_from_ws()
    get_huobi_from_ws()
    # get_huobi_from_ws()