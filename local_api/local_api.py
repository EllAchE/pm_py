from flask import Flask
from polymarket.utils import approve_erc20, load_evm_abi

from polymarket import initialize_identity, buy

app = Flask(__name__)

# 0x18f541b0844BEB2517A7B825a95402227536234b
# Secretary firing by october test market address

# Test trigger url http://127.0.0.1:5000/polybuy/0x18f541b0844BEB2517A7B825a95402227536234b/0.5/1/0.52/1
# invalid url test http://127.0.0.1:5000/polybuy/-1000/-1000/-1000/-1000/-1000

@app.route('/polybuy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def buyOrder(mmAddress, amount, outcomeIndex, minShares, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("minShares", minShares)
    print("gas", gas)

    try:
        amount = float(amount)
        outcomeIndex = int(outcomeIndex)
        gas = int(gas)
        minShares = float(minShares)
        if amount > 1000 or amount < 0:
            return createReturnJson("spend amount must be positive and greater than 1000", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
        elif outcomeIndex > 10 or outcomeIndex < 0:
            return createReturnJson("outcomeindex is invalid, must be 0-10", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
        elif gas < 1:
            return createReturnJson("gas must be greater than 1", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
        elif minShares < amount:
            return createReturnJson("min shares less than amount", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")

    except Exception as e:
        return createReturnJson(e, mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")

    # Actual purchase logic
    w3 = initialize_identity(gas)

    try:
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print('hash made', str(trx_hash))

    return createReturnJson("200 OK", mmAddress, amount, outcomeIndex, minShares, gas, trx_hash)

def createReturnJson(exception, mmAddress, amount, outcomeIndex, minShares, gas, trx_hash):
    return {
        "isError": str(exception),
        "mmAddress": mmAddress,
        "amount": amount,
        "outcomeIndex": outcomeIndex,
        "minShares": minShares,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def preapprove(web3_provider, market_maker_address, amount):
    return approve_erc20(web3_provider, market_maker_address, amount)

def buyPreapprovedAmount(web3_provider, marketMakerAddress, approvedAmount, index, minShares):
    fixed_product_market_maker_address_abi = load_evm_abi('FixedProductMarketMaker.json')

    # Adjust share number to the raw value used by the buy contract
    fixedMinimumShares = int(minShares * (10 ** 6))

    contract = web3_provider.eth.contract(address=marketMakerAddress, abi=fixed_product_market_maker_address_abi)
    trxHash = contract.functions.buy(approvedAmount, index, fixedMinimumShares).transact()
    web3_provider.eth.wait_for_transaction_receipt(trxHash)
    return trxHash


@app.route('/polypreapprove/<mmAddress>/<amount>/<gas>')
def preapproveEndpoint(mmAddress, amount, gas):
    w3 = initialize_identity(gas)
    return preapprove(w3, mmAddress, amount), w3

@app.route('/polypreapprove/<mmAddress>/<amount>/<gas>')
def buyPreapprovedAmountEndpoint(mmAddress, amount, gas):
    return buyPreapprovedAmount(w3, mmAddress, approved_amount, index, minShares) # approved amount nee

app.run()