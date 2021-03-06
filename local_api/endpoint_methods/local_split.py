from .custom_utils import createBuyReturnJson, createSplitReturnJson, EARLY_EXIT_STRING, \
    SUCCESS_RESPONSE_STRING
from polymarket import split, initialize_identity


def localSplit(conditionId, amount, numberOfOutcomes, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("conditionId", conditionId)
    print("amount", amount)
    print("minShares", numberOfOutcomes)
    print("gas", gas)

    try:
        amount = int(amount)
        numberOfOutcomes = int(numberOfOutcomes)
        gas = int(gas)

        if amount > 1000 or amount < 0:
            return createBuyReturnJson("split amount must be positive and less than 1000", conditionId, amount, numberOfOutcomes, gas, EARLY_EXIT_STRING)
        elif numberOfOutcomes > 9 or numberOfOutcomes < 1:
            return createBuyReturnJson("split number of outcomes must be at least 1 and less than 10", conditionId, amount, numberOfOutcomes, gas, EARLY_EXIT_STRING)
        elif gas < 1:
            return createBuyReturnJson("gas must be 1 or greater", conditionId, amount, numberOfOutcomes, gas, EARLY_EXIT_STRING)
        try:
            w3 = initialize_identity(gas)
            trxHash = split(w3, conditionId, numberOfOutcomes, amount)
            return createSplitReturnJson(SUCCESS_RESPONSE_STRING, conditionId, numberOfOutcomes, gas, trxHash)
        except Exception as e:
            return createSplitReturnJson(e, conditionId, numberOfOutcomes, gas, EARLY_EXIT_STRING)

    except Exception as e:
        return createSplitReturnJson(e, conditionId, numberOfOutcomes, gas, EARLY_EXIT_STRING)
