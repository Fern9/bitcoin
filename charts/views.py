import json
import time, datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from apis.huobi.api import HuobiAPI
from apis.okcoin.api import OkAPI

apikey = '668ac363-c3d0-4dee-b6f5-3f237de5878a'
secretkey = 'E8A0BCE0B732927FAC30ADFAAE460232'

ok_api = OkAPI(apikey, secretkey)
huobi_api = HuobiAPI(apikey, secretkey)


def home(request):
    return render_to_response('index.html')


def get_ticker(request):
    res = ok_api.ticker()
    t = int(res['date'])
    value_ok = float(res['ticker']['last'])
    res = huobi_api.ticker()
    value_huobi = float(res['ticker']['last'])

    timeArray = time.localtime(t)
    str_time = time.strftime("%H:%M:%S", timeArray)

    data = {
        "t": str_time,
        "ok": value_ok,
        "huo": value_huobi,
        "diff": value_ok - value_huobi
    }

    return HttpResponse(json.dumps({
        "code": 200,
        "msg": '',
        "data": data
    }))



