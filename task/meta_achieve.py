import sys
sys.path.append('..')
import env
from time import sleep

from datetime import datetime
from task.request import ConcurrentRequest

from apis import ok_api, huobi_api
from charts.models import OKCoinSpot, HuobiSpot, Config
from task.schedule import schedule


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
        huobi.save()


if __name__ == '__main__':

    sch = schedule('get_market', get_market, '2017-01-13 01:19:00')
    while True:
        run = Config.objects.filter(key='get_market_run').first().value
        if int(run):
            if sch.state != 1:
                sch.resume()
            sleep(1)
        else:
            sch.pause()
