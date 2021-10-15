from flask import Flask

from local_api.buy_order import buyEndpoint
from polymarket import initialize_identity, buy

app = Flask(__name__)

# 0x18f541b0844BEB2517A7B825a95402227536234b
# Secretary firing by october test market address

# Test trigger url http://127.0.0.1:5000/polybuy/0x18f541b0844BEB2517A7B825a95402227536234b/0.5/1/0.52/1

@app.route('/polybuy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def buyOrder(mmAddress, amount, outcomeIndex, minShares, gas):
    return buyEndpoint(amount, gas, minShares, mmAddress, outcomeIndex)







app.run()