from polymarket import merge, initialize_identity
from local_api.endpoint_methods.utils import createMergeReturnJson, EARLY_EXIT_STRING


def mergeShares(conditionId, numberOfOutcomes, amount, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("conditionId", conditionId)
    print("numberOfOutcomes", numberOfOutcomes)
    print("amount", amount)
    print("gas", gas)

    try:
        gas = int(gas)
        numberOfOutcomes = int(numberOfOutcomes)
        if gas < 1:
            return createMergeReturnJson("gas must be 1 or greater", conditionId, numberOfOutcomes, amount, gas, EARLY_EXIT_STRING)
        if numberOfOutcomes < 2 or numberOfOutcomes > 10:
            return createMergeReturnJson("number of outcomes must be at least 2 and less than 10", conditionId, numberOfOutcomes, amount, gas, EARLY_EXIT_STRING)
    except Exception as e:
        return createMergeReturnJson(e, conditionId, numberOfOutcomes, amount, gas, EARLY_EXIT_STRING)

    try:
        w3Provider = initialize_identity(gas)
        trxHash = merge(w3Provider, conditionId, numberOfOutcomes, amount)
        return createMergeReturnJson("200 OK", conditionId, numberOfOutcomes, amount, gas, trxHash)
    except Exception as e:
        return createMergeReturnJson(e, conditionId, numberOfOutcomes, amount, gas, EARLY_EXIT_STRING)
