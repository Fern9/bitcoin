import json
import thread
import websocket
import ssl
from gevent import sleep


class WS:
    def __init__(self, uri, header=None, debug=True):
        websocket.enableTrace(debug)
        self.ws = websocket.WebSocketApp(uri,
                                         header=header,
                                         on_message=self._on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)

        self.ws.on_open = self.on_open

    def _on_message(self, ws, message):
        print 'message:', message
        data = json.loads(message)
        self.on_message(ws, data)

    def on_message(self, ws, data):
        pass

    def on_error(self, ws, error):
        print 'error:', error

    def on_close(self, ws):
        print "### close ###"

    def on_open(self, ws):
        print "## open ##"

    def start(self):
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def asyc_start(self):
        thread.start_new_thread(self.start, ())

    def send(self, data, txt=False):
        if not txt:
            data = json.dumps(data)
        self.ws.send(data)


# if __name__ == '__main__':
#     ws = WS('wss://real.okcoin.cn:10440/websocket/okcoinapi')
#     ws.asyc_start()
#     print 'end'
#     index = 0
#     while True:
#         sleep(5)
#         print 'sleep 5'



if __name__ == '__main__':
    def open(ws):
        print 'send---'
        ws.send({
            'version': 1,
            'msgType': 'reqSymbolList',
        })


    # ws = WS('wss://hq.huobi.com/websocket/ooUNulSc43H0xwKnT10i')
    # ws.on_open = open

    # ws.asyc_start()
    ws = websocket.create_connection("wss://hq.huobi.com", subprotocols=["binary", "base64"])
    result = ws.recv()
    print result
    # ws.send()
    while True:
        sleep(0.2)
        # open(ws)
        sleep(10)

    print 'end'
