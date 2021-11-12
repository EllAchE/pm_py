from polymarket import initialize_identity, buy, load_evm_abi

from local_api.endpoint_methods.utils import createBuyReturnJson, EARLY_EXIT_STRING, SUCCESS_RESPONSE_STRING

# @app.route('/poly/unapproved_buy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def buyOrder(mmAddress, amount, outcomeIndex, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("gas", gas)

    try:
        amount = float(amount)
        minShares = amount / 0.977
        minShares = float(minShares)
        print("minShares", minShares)
        outcomeIndex = int(outcomeIndex)
        gas = int(gas)

        if amount > 1000 or amount < 0:
            return createBuyReturnJson("spend amount must be positive and less than 1000", mmAddress, amount, outcomeIndex, minShares, gas, EARLY_EXIT_STRING)
        elif outcomeIndex > 10 or outcomeIndex < 0:
            return createBuyReturnJson("outcomeIndex is invalid, must be 0-10", mmAddress, amount, outcomeIndex, minShares, gas, EARLY_EXIT_STRING)
        elif gas < 1:
            return createBuyReturnJson("gas must be 1 or greater", mmAddress, amount, outcomeIndex, minShares, gas, EARLY_EXIT_STRING)
        elif minShares < amount:
            return createBuyReturnJson("min shares less than amount", mmAddress, amount, outcomeIndex, minShares, gas, EARLY_EXIT_STRING)

    except Exception as e:
        return createBuyReturnJson(e, mmAddress, amount, outcomeIndex, minShares, gas, EARLY_EXIT_STRING)

    try:
        # Actual purchase logic
        w3 = initialize_identity(gas)
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print('hash made', str(trx_hash))

    return createBuyReturnJson(SUCCESS_RESPONSE_STRING, mmAddress, amount, outcomeIndex, minShares, gas, trx_hash)
