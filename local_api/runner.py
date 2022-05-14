from flask import Flask

from PreappovePersistence import PreapprovePersistence
from endpoint_methods.local_buy_approved import buyPreapprovedAmount
from endpoint_methods.local_buy_unapproved import buyOrder
from endpoint_methods.local_merge import mergeShares
from endpoint_methods.local_preapprove import preapproveAmount
from endpoint_methods.local_redeem import redeemTokens
from endpoint_methods.local_sell import sellAmount
from endpoint_methods.local_positions import localListPositions
from endpoint_methods.local_split import localSplit

app = Flask(__name__)
persistObj = PreapprovePersistence() # todo persist approvals differently

# Test trigger url http://127.0.0.1:5000/polybuy
# Test trigger url http://127.0.0.1:5000/polypositions
# invalid url test http://127.0.0.1:5000/polybuy/-1000/-1000/-1000/-1000/-1000

# Test trigger url http://127.0.0.1:5000/poly/ping
@app.route('/poly/ping')
def ping():
    print("ping")
    return "pong"

# Test trigger url http://127.0.0.1:5000/poly/unapproved_buy/ # todo test
@app.route('/poly/unapproved_buy/<mmAddress>/<amount>/<outcomeIndex>/<gas>')
def unapprovedBuyOrderEndpoint(mmAddress, amount, outcomeIndex, gas):
    return buyOrder(mmAddress, amount, outcomeIndex, gas)

# Test trigger url http://127.0.0.1:5000/poly/preapprove # todo test
@app.route('/poly/preapprove/<mmAddress>/<amount>/<gas>')
def preapproveEndpoint(mmAddress, amount, gas):
    return preapproveAmount(amount, gas, mmAddress, persistObj)

# Test trigger url http://127.0.0.1:5000/poly/preapproved_buy # todo test
@app.route('/poly/preapproved_buy/<mmAddress>/<index>') # should be able to buy without any of the args here. Currently only persists 1 preapprove obj in memory. Must fix overwrite
def preapprovedBuyEndpoint(mmAddress, index):
    return buyPreapprovedAmount(persistObj.getWeb3Provider(), mmAddress, persistObj.getPreapprovedAmount(), index, persistObj.getPreapprovedAmount())

# Test trigger url http://127.0.0.1:5000/poly/sell_amount # todo test
@app.route('/poly/sell_amount/<mmAddress>/<amount>/<outcomeIndex>/<gas>')
def sellAmountEndpoint(mmAddress, amount, outcomeIndex, gas):
    return sellAmount(mmAddress, amount, outcomeIndex, gas)

# Test trigger url http://127.0.0.1:5000/poly/split # todo test
@app.route('/poly/split/<conditionId>/<amount>/<numberOfOutcomes>/<gas>')
def splitSharesEndpoint(conditionId, amount, numberOfOutcomes, gas):
    return localSplit(conditionId, amount, numberOfOutcomes, gas)

# Test trigger url http://127.0.0.1:5000/poly/merge # todo test
@app.route('/poly/merge/<conditionId>/<amount>/<numberOfOutcomes>/<gas>')
def mergeSharesEndpoint(conditionId, numberOfOutcomes, amount, gas):
    return mergeShares(conditionId, numberOfOutcomes, amount, gas)

# Test trigger url http://127.0.0.1:5000/poly/positions
@app.route('/poly/positions')
def listPositionsEndpoint():
    localListPositions()
    return "Should've listed positions in console where Flask app is running"

# Test trigger url http://127.0.0.1:5000/poly/redeem/
@app.route('/poly/redeem/<conditionId>/<numberOfOutcomes>/<gas>')
def redeemTokensEndpoint(conditionId, numberOfOutcomes, gas):
    return redeemTokens(conditionId, numberOfOutcomes, gas)

app.run()

# # Test trigger url http://127.0.0.1:5000/poly/sell_shares
# @app.route('/poly/sell_shares/<conditionId>/<mmAddress>/<outcomeIndex>/<numberOfShares>/<numberOfOutcomes>/<slippage>/<fee>/<gas>')
# def sellSharesEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
#     return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)



# # Test trigger url http://127.0.0.1:5000/
# @app.route('/poly/sell_shares_with_slug/<slug>/<slippage>/<fee>/<gas>')
# def sellSharesWithSlugEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
#     return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)





#
# # Test trigger url http://127.0.0.1:5000/ping_save/
# @app.route('/ping_save/<save>') # only created/hit this endpoint for tests
# def pingSave(save):
#     persistObj.addPreapproval(save, 5, 20)
#     return "saved {}. Should return the number 5 when you run this test".format(save)
#
# # Test trigger url http://127.0.0.1:5000/ping_return_save/
# @app.route('/ping_return_save/<save>')
# def pingReturn(save):
#     obj = persistObj.getPreapproval(save)
#     return str(obj.minShares)

