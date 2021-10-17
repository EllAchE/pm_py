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

def createRedeemReturnJson(exception, conditionId, numberOfOutcomes, gas, trx_hash):
    return {
        "isError": str(exception),
        "conditionId": conditionId,
        "numberOfOutcomes": numberOfOutcomes,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def createMergeReturnJson(exception, conditionId, numberOfOutcomes, amount, gas, trx_hash):
    return {
        "isError": str(exception),
        "conditionId": conditionId,
        "numberOfOutcomes": numberOfOutcomes,
        "amount": amount,
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

def createSellReturnJson(exception, mmAddress, amount, outcomeIndex, gas, trx_hash):
    return {
        "isError": str(exception),
        "mmAddress": mmAddress,
        "amount": amount,
        "outcomeIndex": outcomeIndex,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def createSlugSellReturnJson(exception, slug, outcomeLabel, numberOfShares, slippage, gas, trx_hash):
    return {
        "isError": str(exception),
        "slug": slug,
        "outcomeLabel": outcomeLabel,
        "numberOfShares": numberOfShares,
        "slippage": slippage,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }