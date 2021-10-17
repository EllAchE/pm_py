from flask import Flask

from local_api.PreappovePersistence import PreapprovePersistence
from local_api.local_buy import buyOrder, buyPreapprovedAmount
from local_api.local_preapprove import preapproveAmount
from local_api.local_redeem import redeemTokens
from local_api.local_sell import sellAmount
from local_api.local_sell_shares import sellShares
from local_api.local_split import localSplit

app = Flask(__name__)
persistObj = PreapprovePersistence() # todo persist approvals differently

# Test trigger url http://127.0.0.1:5000/polybuy/
# invalid url test http://127.0.0.1:5000/polybuy/-1000/-1000/-1000/-1000/-1000

@app.route('/polybuy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def unapprovedBuyOrderEndpoint(mmAddress, amount, outcomeIndex, minShares, gas):
    return buyOrder(mmAddress, amount, outcomeIndex, minShares, gas)

@app.route('/polypreapprove/<mmAddress>/<amount>/<gas>')
def preapproveEndpoint(mmAddress, amount, gas):
    return preapproveAmount(amount, gas, mmAddress)

@app.route('/polypreapprovebuy/<mmAddress>/<index>') # should be able to buy without any of the args here. Currently only persists 1 preapprove obj in memory. Must fix overwrite
def preapprovedBuyEndpoint(mmAddress, index):
    return buyPreapprovedAmount(persistObj.getWeb3Provider(), mmAddress, persistObj.getPreapprovedAmount(), index, persistObj.getPreapprovedAmount())

@app.route('/polyredeem/<conditionId>/<numberOfOutcomes>')
def redeemTokensEndpoint(conditionId, numberOfOutcomes):
    return redeemTokens(persistObj.getWeb3Provider(), conditionId, numberOfOutcomes)

@app.route('/polysplit/<conditionId>/<amount>/<numberOfOutcomes>')
def splitSharesEndpoint(conditionId, amount, numberOfOutcomes):
    return localSplit(conditionId, amount, numberOfOutcomes)

@app.route('/polysell_amount/<mmAddress>/<amount>/<outcomeIndex>')
def sellAmountEndpoint(conditionId, amount, numberOfOutcomes):
    return sellAmount(conditionId, amount, numberOfOutcomes)

@app.route('/polysell_shares/<conditionId>/<mmAddress>/<outcomeIndex>/<numberOfShares>/<outcomeIndex>/<numberOfOutcomes>/<slippage>/<fee>/<gas>')
def sellSharesEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
    return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)

@app.route('/polysell_shares_with_slug/<slug>/<slippage>/<fee>/<gas>')
def sellSharesEndpoint(conditionId, mmAddress, outcomeIndex, numberOfShares, numberOfOutcomes, slippage, fee, gas):
    return sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas)


app.run()