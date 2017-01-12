import json
import time, datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response

from apis import ok_api, huobi_api


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
        "diff": value_huobi - value_ok
    }

    return HttpResponse(json.dumps({
        "code": 200,
        "msg": '',
        "data": data
    }))



