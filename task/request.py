import sys
from time import time

import gevent
import requests
from gevent import monkey
from gevent.pool import Group

if 'threading' in sys.modules:
    del sys.modules['threading']
monkey.patch_all()


class ConcurrentRequest:
    def __init__(self):
        self.group = Group()
        self.ans = []
        self.grs = []

    def add(self, func, args):
        g = gevent.spawn(func, *args)
        self.grs.append(g)
        self.group.add(g)

    def start(self, timeout=0.9):
        self.group.join(timeout=timeout, raise_error=True)
        return [g.value for g in self.grs]


if __name__ == '__main__':
    def req(url):
        req = requests.get(url)
        return req


    s = time()
    creq = ConcurrentRequest()
    for i in xrange(200):
        creq.add(req, ('https://baidu.com',))


    ans = creq.start(200)
    e = time()
    print len(ans), e - s
    print [r.text for r in ans]

    s = time()
    for i in xrange(200):
        r = req('https://baidu.com')
    e = time()
    print e - s
