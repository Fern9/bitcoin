from time import time

import requests

if __name__ == '__main__':
    def req(url):
        req = requests.get(url)
        return req

    s = time()
    for i in xrange(200):
        r = req('https://baidu.com')
    e = time()
    print e - s