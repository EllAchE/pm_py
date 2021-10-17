from polymarket import sell, initialize_identity


def sellAmount(mmAddress, amount, outcomeIndex, gas):
    w3Provider = initialize_identity(gas)
    trxHash = sell(w3Provider, mmAddress, amount, outcomeIndex)
    return trxHash