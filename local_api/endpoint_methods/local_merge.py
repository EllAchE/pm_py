from polymarket import merge, initialize_identity
from local_api.endpoint_methods.utils import createMergeReturnJson

def mergeShares(conditionId, numberOfOutcomes, amount, gas):
    w3Provider = initialize_identity(gas)
    trxHash = merge(w3Provider, conditionId, numberOfOutcomes, amount)
    return createMergeReturnJson("200 OK", conditionId, numberOfOutcomes, amount, gas, trxHash)