from local_api.endpoint_methods.utils import createRedeemReturnJson, EARLY_EXIT_STRING, SUCCESS_RESPONSE_STRING
from polymarket import redeem, initialize_identity

def redeemTokens(conditionId, numberOfOutcomes, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("conditionId", conditionId)
    print("numberOfChoices", numberOfOutcomes)
    print("gas", gas)

    try:
        gas = int(gas)
        numberOfOutcomes = int(numberOfOutcomes)
        if gas < 1:
            return createRedeemReturnJson("gas must be 1 or greater", conditionId, numberOfOutcomes, gas, EARLY_EXIT_STRING)
        if numberOfOutcomes < 2 or numberOfOutcomes > 10:
            return createRedeemReturnJson("number of outcomes must be at least 2 and less than 10", conditionId, numberOfOutcomes, gas, EARLY_EXIT_STRING)
    except Exception as e:
        return createRedeemReturnJson(e, conditionId, numberOfOutcomes, gas, EARLY_EXIT_STRING)

    try:
        # Actual purchase logic
        print('initializing identity')
        w3 = initialize_identity(gas)
        print('initialized identity')
        trxHash = redeem(w3, conditionId, numberOfOutcomes)
        return createRedeemReturnJson(SUCCESS_RESPONSE_STRING, conditionId, numberOfOutcomes, gas, trxHash)
    except Exception as e:
        return createRedeemReturnJson(e, conditionId, numberOfOutcomes, gas, EARLY_EXIT_STRING)
