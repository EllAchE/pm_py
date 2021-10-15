def createReturnJson(exception, mmAddress, amount, outcomeIndex, minShares, gas, trx_hash):
    return {
        "isError": str(exception),
        "mmAddress": mmAddress,
        "amount": amount,
        "outcomeIndex": outcomeIndex,
        "minShares": minShares,
        "gas": gas,
        "transactionHash": str(trx_hash)
    }