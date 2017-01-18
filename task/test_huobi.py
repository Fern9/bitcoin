from huobi_client import StreamingClient


def on_message(data):
    print(data)

sclient = StreamingClient()
sclient.subscribe('marketOverview')
sclient.connect(on_message)