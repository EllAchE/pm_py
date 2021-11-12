from polymarket import sell, initialize_identity
from local_api.endpoint_methods.utils import createSellReturnJson, EARLY_EXIT_STRING, SUCCESS_RESPONSE_STRING


def sellAmount(mmAddress, amount, outcomeIndex, maxShares, gas):
    print("received args")
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("gas", gas)

    try:
        amount = float(amount)
        maxShares = amount / 0.002 # very low threshold, 2 tenths cent lowest
        maxShares = float(maxShares)
        print("maxShares", maxShares)
        outcomeIndex = int(outcomeIndex)
        gas = int(gas)

        if outcomeIndex > 10 or outcomeIndex < 0:
            return createSellReturnJson("outcomeindex is invalid, must be 0-10", mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)
        if gas < 1:
            return createSellReturnJson("gas must be 1 or greater", mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)
        if amount < 0 or amount > 1000:
            return createSellReturnJson("sell amount must be from 0-1000", mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)
        if maxShares < 0:
            return createSellReturnJson("maxShares must be greater than zero", mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)

    except Exception as e:
        return createSellReturnJson(e, mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)

    w3Provider = initialize_identity(gas)
    trxHash = sell(w3Provider, mmAddress, amount, outcomeIndex, maxShares)
    return createSellReturnJson(SUCCESS_RESPONSE_STRING, mmAddress, amount, outcomeIndex, gas, maxShares, trxHash)