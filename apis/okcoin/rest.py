import json
from time import time

import requests


class BaseHTTPs:
    def get(self, url, data=None, load=True):
        s = time()
        res = requests.get(url=url, params=data, timeout=0.5)
        e = time()
        print 'ok:', (e - s) * 1000
        if load:
            return json.loads(res.text)
        else:
            return res.text
