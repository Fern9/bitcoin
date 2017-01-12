from apis.huobi.api import HuobiAPI
from apis.okcoin.api import OkAPI
from charts.models import OKCoinSpot
from django.shortcuts import render_to_response, HttpResponse

apikey = '668ac363-c3d0-4dee-b6f5-3f237de5878a'
secretkey = 'E8A0BCE0B732927FAC30ADFAAE460232'

ok_api = OkAPI(apikey, secretkey)
huobi_api = HuobiAPI(apikey, secretkey)


def test_data(request, method=['GET', 'POST']):
    res = ok_api.ticker()
    okcoin = OKCoinSpot(date_stamp=res['date'], sell=res['ticker']['sell'], buy=res['ticker']['buy'],
                        last=res['ticker']['last'], vol=res['ticker']['vol'], high=res['ticker']['high'],
                        low=res['ticker']['low'])
    okcoin.save()
    # return render_to_response('charts/index.html')
    return HttpResponse('hello')


