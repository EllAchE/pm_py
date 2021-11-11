from polymarket import initialize_identity, buy, load_evm_abi

from local_api.endpoint_methods.utils import createBuyReturnJson, EARLY_EXIT_STRING, SUCCESS_RESPONSE_STRING

# @app.route('/polypreapprovebuy/<mmAddress>/<index>') # should be able to buy without any of the args here. Currently only persists 1 preapprove obj in memory. Must fix overwrite
def buyPreapprovedAmount(w3provider, mmAddress, amount, outcomeIndex, minShares):
    print("received args")
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("minShares", minShares)

    try:
        amount = float(amount)
        outcomeIndex = int(outcomeIndex)
        minShares = float(minShares)
        if amount > 1000 or amount < 0:
            return createBuyReturnJson("spend amount must be positive and less than 1000", mmAddress, amount,
                                       outcomeIndex, minShares, "gas preapproved", EARLY_EXIT_STRING)
        elif outcomeIndex > 10 or outcomeIndex < 0:
            return createBuyReturnJson("outcomeIndex is invalid, must be 0-10", mmAddress, amount, outcomeIndex,
                                       minShares, "gas preapproved", EARLY_EXIT_STRING)
        elif minShares < amount:
            return createBuyReturnJson("min shares less than amount", mmAddress, amount, outcomeIndex, minShares, gas,
                                       EARLY_EXIT_STRING)
    except Exception as e:
        return createBuyReturnJson(e, mmAddress, amount, outcomeIndex, minShares, "gas preapproved", EARLY_EXIT_STRING)

    try:
        # Actual purchase logic
        fixed_product_market_maker_address_abi = load_evm_abi('FixedProductMarketMaker.json')

        # Adjust share number to the raw value used by the buy contract
        fixedMinimumShares = int(minShares * (10 ** 6))

        contract = w3provider.eth.contract(address=mmAddress, abi=fixed_product_market_maker_address_abi)
        trxHash = contract.functions.buy(amount, outcomeIndex, fixedMinimumShares).transact()

        w3provider.eth.wait_for_transaction_receipt(trxHash)
        return createBuyReturnJson(SUCCESS_RESPONSE_STRING, mmAddress, amount, outcomeIndex, minShares, "gas preapproved", trxHash)
    except Exception as e:
        return createBuyReturnJson(e, mmAddress, amount, outcomeIndex, minShares, "gas preapproved", EARLY_EXIT_STRING)


