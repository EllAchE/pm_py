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

def createSellReturnJson(exception, mmAddress, amount, outcomeIndex, maxShares, gas, trx_hash):
    return {
        "isError": str(exception),
        "mmAddress": mmAddress,
        "amount": amount,
        "outcomeIndex": outcomeIndex,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

def createSellSharesReturnJson(exception, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas, trx_hash):
    return {
        "isError": str(exception),
        "mmAddress": mmAddress,
        "numberOfShares": numberOfShares,
        "outcomeIndex": outcomeIndex,
        "numberOfOutcomes": numberOfOutcomes,
        "slippage": slippage,
        "fee": fee,
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

def createPreapprovalReturnJson(exception, amount, gas, mmAddress, trx_hash):
    return {
        "isError": str(exception),
        "amount": amount,
        "mmAddress": mmAddress,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }

EARLY_EXIT_STRING = "Execution exited early"
SUCCESS_RESPONSE_STRING = "200 OK"