from polymarket import sell, initialize_identity
from local_api.endpoint_methods.utils import createSellReturnJson

def sellAmount(mmAddress, amount, outcomeIndex, gas):
    w3Provider = initialize_identity(gas)
    trxHash = sell(w3Provider, mmAddress, amount, outcomeIndex)
    return createSellReturnJson("200 OK", mmAddress, amount, outcomeIndex, gas, trxHash)