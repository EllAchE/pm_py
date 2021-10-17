def createBuyReturnJson(exception, mmAddress, amount, outcomeIndex, minShares, gas, trx_hash):
    return {
        "isError": str(exception),
        "mmAddress": mmAddress,
        "amount": amount,
        "outcomeIndex": outcomeIndex,
        "minShares": minShares,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def createRedeemReturnJson(exception, conditionId, numberOfChoices, gas, trx_hash):
    return {
        "isError": str(exception),
        "conditionId": conditionId,
        "numberOfChoices": numberOfChoices,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def createSplitReturnJson(exception, conditionId, numberOfChoices, gas, trx_hash):
    return {
        "isError": str(exception),
        "conditionId": conditionId,
        "numberOfChoices": numberOfChoices,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def createSellReturnJson(exception, mmAddress, amount, index, trx_hash):
    return {
        "isError": str(exception),
        "conditionId": conditionId,
        "numberOfChoices": numberOfChoices,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }