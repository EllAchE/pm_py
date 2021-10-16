from polymarket import initialize_identity, buy, load_evm_abi
from local_api.utils import createBuyReturnJson

def buyOrder(mmAddress, amount, outcomeIndex, minShares, gas):
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
        if amount > 1000 or amount < 0:
            return createBuyReturnJson("spend amount must be positive and greater than 1000", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
        elif outcomeIndex > 10 or outcomeIndex < 0:
            return createBuyReturnJson("outcomeindex is invalid, must be 0-10", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
        elif gas < 1:
            return createBuyReturnJson("gas must be 1 or greater", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")
        elif minShares < amount:
            return createBuyReturnJson("min shares less than amount", mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")

    except Exception as e:
        return createBuyReturnJson(e, mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")

    # Actual purchase logic
    w3 = initialize_identity(gas)

    try:
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print('hash made', str(trx_hash))

    return createBuyReturnJson("200 OK", mmAddress, amount, outcomeIndex, minShares, gas, trx_hash)

def buyPreapprovedAmount(web3_provider, marketMakerAddress, approvedAmount, index, minShares):
    fixed_product_market_maker_address_abi = load_evm_abi('FixedProductMarketMaker.json')

    # Adjust share number to the raw value used by the buy contract
    fixedMinimumShares = int(minShares * (10 ** 6))

    contract = web3_provider.eth.contract(address=marketMakerAddress, abi=fixed_product_market_maker_address_abi)
    trxHash = contract.functions.buy(approvedAmount, index, fixedMinimumShares).transact()
    web3_provider.eth.wait_for_transaction_receipt(trxHash)
    return trxHash
