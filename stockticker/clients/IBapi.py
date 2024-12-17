import logging
import threading
import time

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def tickPrice(self, reqId, tickType, price, attrib):
        print("reqId {0} - tickType {1} - price {2}".format(reqId, tickType, price))


app = IBapi()
app.connect("127.0.0.1", 4001, clientId=1)


def run_loop():
    app.run()


api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1)
apple_contract = Contract()
apple_contract.symbol = "VUSA"
apple_contract.secType = "STK"
apple_contract.exchange = "SMART"
apple_contract.currency = "EUR"

app.reqMarketDataType(4)
app.reqMktData(1, apple_contract, "", False, False, [])
