def buyEndpoint(amount, gas, minShares, mmAddress, outcomeIndex):
    # Print arguments to py console. Likely unseen
    print("received args")
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("minShares", minShares)
    print("gas", gas)
    try:
        amount = float(amount)
        outcomeIndex = int(outcomeIndex)
        gas = int(gas)
        minShares = float(minShares)
    except Exception as e:
        return createReturnJson(e, mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
    # Actual purchase logic
    w3 = initialize_identity(gas)
    try:
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print('hash made', str(trx_hash))
    return createReturnJson("200 OK", mmAddress, amount, outcomeIndex, minShares, gas, trx_hash)