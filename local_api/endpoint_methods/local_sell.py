from polymarket import sell, initialize_identity
from local_api.endpoint_methods.utils import createSellReturnJson, EARLY_EXIT_STRING


def sellAmount(mmAddress, amount, outcomeIndex, maxShares, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("maxShares", maxShares)
    print("gas", gas)

    try:
        amount = float(amount)
        outcomeIndex = int(outcomeIndex)
        gas = int(gas)
        if outcomeIndex > 10 or outcomeIndex < 0:
            return createSellReturnJson("outcomeindex is invalid, must be 0-10", mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)
        if gas < 1:
            return createSellReturnJson("gas must be 1 or greater", mmAddress, amount, outcomeIndex, maxShares, gas, EARLY_EXIT_STRING)

    except Exception as e:
        pass

    w3Provider = initialize_identity(gas)
    trxHash = sell(w3Provider, mmAddress, amount, outcomeIndex, maxShares)
    return createSellReturnJson("200 OK", mmAddress, amount, outcomeIndex, gas, trxHash)