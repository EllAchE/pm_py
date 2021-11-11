from flask import Flask

from local_api.PreappovePersistence import PreapprovePersistence
from local_api.endpoint_methods.local_buy_approved import buyPreapprovedAmount
from local_api.endpoint_methods.local_buy_unapproved import buyOrder
from local_api.endpoint_methods.local_merge import mergeShares
from local_api.endpoint_methods.local_preapprove import preapproveAmount
from local_api.endpoint_methods.local_redeem import redeemTokens
from local_api.endpoint_methods.local_sell import sellAmount
from local_api.endpoint_methods.local_sell_shares import sellShares
from local_api.endpoint_methods.local_split import localSplit
from local_api.endpoint_methods.local_positions import localListPositions

app = Flask(__name__)
persistObj = PreapprovePersistence() # todo persist approvals differently

# Test trigger url http://127.0.0.1:5000/polybuy/
# Test trigger url http://127.0.0.1:5000/polypositions/
# invalid url test http://127.0.0.1:5000/polybuy/-1000/-1000/-1000/-1000/-1000

# Test trigger url http://127.0.0.1:5000/ping/
@app.route('/ping')
def ping():
    return "pong"

@app.route('/polybuy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def unapprovedBuyOrderEndpoint(mmAddress, amount, outcomeIndex, minShares, gas):
    return buyOrder(mmAddress, amount, outcomeIndex, minShares, gas)

@app.route('/polypreapprove/<mmAddress>/<amount>/<gas>')
def preapproveEndpoint(mmAddress, amount, gas):
    return preapproveAmount(amount, gas, mmAddress)

@app.route('/polypreapprovebuy/<mmAddress>/<index>') # should be able to buy without any of the args here. Currently only persists 1 preapprove obj in memory. Must fix overwrite
def preapprovedBuyEndpoint(mmAddress, index):
    return buyPreapprovedAmount(persistObj.getWeb3Provider(), mmAddress, persistObj.getPreapprovedAmount(), index, persistObj.getPreapprovedAmount())

@app.route('/polysell_amount/<mmAddress>/<amount>/<outcomeIndex>/<gas>/<maxShares>')
def sellAmountEndpoint(mmAddress, amount, outcomeIndex, gas, maxShares):
    return sellAmount(mmAddress, amount, outcomeIndex, gas, maxShares)

@app.route('/polysell_shares/<conditionId>/<mmAddress>/<outcomeIndex>/<numberOfShares>/<numberOfOutcomes>/<slippage>/<fee>/<gas>')
def sellSharesEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
    return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)

@app.route('/polyredeem/<conditionId>/<numberOfOutcomes>/<gas>')
def redeemTokensEndpoint(conditionId, numberOfOutcomes, gas):
    return redeemTokens(conditionId, numberOfOutcomes, gas)

@app.route('/polysplit/<conditionId>/<amount>/<numberOfOutcomes>/<gas>')
def splitSharesEndpoint(conditionId, amount, numberOfOutcomes, gas):
    return localSplit(conditionId, amount, numberOfOutcomes, gas)

@app.route('/polysell_shares_with_slug/<slug>/<slippage>/<fee>/<gas>')
def sellSharesWithSlugEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
    return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)

@app.route('/polymerge/<conditionId>/<numberOfOutcomes>/<amount>/<gas>')
def mergeSharesEndpoint(conditionId, numberOfOutcomes, amount, gas):
    return mergeShares(conditionId, numberOfOutcomes, amount, gas)

@app.route('/polypositions/')
def listPositionsEndpoint():
    return localListPositions()

app.run()