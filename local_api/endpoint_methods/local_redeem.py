from local_api.endpoint_methods.utils import createRedeemReturnJson
from polymarket import redeem, initialize_identity

def redeemTokens(conditionId, numberOfChoices, gas):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("conditionId", conditionId)
    print("numberOfChoices", numberOfChoices)
    print("gas", gas)

    try:
        gas = int(gas)
        numberOfChoices = int(numberOfChoices)
        if gas < 1:
            return createRedeemReturnJson("gas must be 1 or greater", conditionId, numberOfChoices, gas, "Execution exited early")
    except Exception as e:
        return createRedeemReturnJson(e, conditionId, numberOfChoices, gas, "Execution exited early")

    try:
        # Actual purchase logic
        w3 = initialize_identity(gas)
        trxHash = redeem(w3, conditionId, numberOfChoices)
        return createRedeemReturnJson("200 OK", conditionId, numberOfChoices, gas, trxHash)
    except Exception as e:
        return createRedeemReturnJson(e, conditionId, numberOfChoices, gas, "Execution exited early")
