from ib_insync import IB, Stock

ib = IB()
ib.connect(port=30004, clientId=1)

nflx_contract = Stock("VUSA", "SMART", "EUR")
ib.qualifyContracts(nflx_contract)
ib.reqMarketDataType(4)
data = ib.reqMktData(nflx_contract)
ib.sleep(10)
print(data.marketPrice())
