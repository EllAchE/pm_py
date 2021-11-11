from flask import Flask

from local_api.PreappovePersistence import PreapprovePersistence
from local_api.endpoint_methods.local_buy_approved import buyPreapprovedAmount
from local_api.endpoint_methods.local_buy_unapproved import buyOrder
from local_api.endpoint_methods.local_merge import mergeShares
from local_api.endpoint_methods.local_preapprove import preapproveAmount
from local_api.endpoint_methods.local_sell import sellAmount
from local_api.endpoint_methods.local_sell_shares import sellShares
from local_api.endpoint_methods.local_positions import localListPositions

app = Flask(__name__)
persistObj = PreapprovePersistence() # todo persist approvals differently

# Test trigger url http://127.0.0.1:5000/polybuy
# Test trigger url http://127.0.0.1:5000/polypositions
# invalid url test http://127.0.0.1:5000/polybuy/-1000/-1000/-1000/-1000/-1000

# Test trigger url http://127.0.0.1:5000/ping
@app.route('/ping')
def ping():
    print("ping")
    return "pong"

# Test trigger url http://127.0.0.1:5000/polybuy/
@app.route('/poly/unapproved_buy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def unapprovedBuyOrderEndpoint(mmAddress, amount, outcomeIndex, minShares, gas):
    return buyOrder(mmAddress, amount, outcomeIndex, minShares, gas)

# Test trigger url http://127.0.0.1:5000/
@app.route('/poly/preapprove/<mmAddress>/<amount>/<gas>')
def preapproveEndpoint(mmAddress, amount, gas):
    return preapproveAmount(amount, gas, mmAddress)

# Test trigger url http://127.0.0.1:5000/
@app.route('/poly/preapproved_buy/<mmAddress>/<index>') # should be able to buy without any of the args here. Currently only persists 1 preapprove obj in memory. Must fix overwrite
def preapprovedBuyEndpoint(mmAddress, index):
    return buyPreapprovedAmount(persistObj.getWeb3Provider(), mmAddress, persistObj.getPreapprovedAmount(), index, persistObj.getPreapprovedAmount())

# Test trigger url http://127.0.0.1:5000/
@app.route('/poly/sell_amount/<mmAddress>/<amount>/<outcomeIndex>/<gas>/<maxShares>')
def sellAmountEndpoint(mmAddress, amount, outcomeIndex, gas, maxShares):
    return sellAmount(mmAddress, amount, outcomeIndex, gas, maxShares)

# Test trigger url http://127.0.0.1:5000/poly/sell_shares # todo test
@app.route('/poly/sell_shares/<conditionId>/<mmAddress>/<outcomeIndex>/<numberOfShares>/<numberOfOutcomes>/<slippage>/<fee>/<gas>')
def sellSharesEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
    return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)

# Test trigger url http://127.0.0.1:5000/poly/merge # todo test
@app.route('/poly/merge/<conditionId>/<numberOfOutcomes>/<amount>/<gas>')
def mergeSharesEndpoint(conditionId, numberOfOutcomes, amount, gas):
    return mergeShares(conditionId, numberOfOutcomes, amount, gas)

# Test trigger url http://127.0.0.1:5000/poly/positions. # todo test Works but very slowly. May cache results in terminal
@app.route('/poly/positions')
def listPositionsEndpoint():
    localListPositions()
    return "Should've listed positions in console where Flask app is running"

app.run()

# # Test trigger url http://127.0.0.1:5000/
# @app.route('/poly/split/<conditionId>/<amount>/<numberOfOutcomes>/<gas>')
# def splitSharesEndpoint(conditionId, amount, numberOfOutcomes, gas):
#     return localSplit(conditionId, amount, numberOfOutcomes, gas)

# # Test trigger url http://127.0.0.1:5000/
# @app.route('/poly/sell_shares_with_slug/<slug>/<slippage>/<fee>/<gas>')
# def sellSharesWithSlugEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
#     return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)


# # Test trigger url http://127.0.0.1:5000/
# @app.route('/poly/redeem/<conditionId>/<numberOfOutcomes>/<gas>')
# def redeemTokensEndpoint(conditionId, numberOfOutcomes, gas):
#     return redeemTokens(conditionId, numberOfOutcomes, gas)


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

