from polymarket import initialize_identity, buy, load_evm_abi

from local_api.endpoint_methods.utils import createBuyReturnJson, EARLY_EXIT_STRING, SUCCESS_RESPONSE_STRING

# @app.route('/polypreapprovebuy/<mmAddress>/<index>') # should be able to buy without any of the args here. Currently only persists 1 preapprove obj in memory. Must fix overwrite
def buyPreapprovedAmount(web3_provider, marketMakerAddress, approvedAmount, index, minShares):
    fixed_product_market_maker_address_abi = load_evm_abi('FixedProductMarketMaker.json')

    # Adjust share number to the raw value used by the buy contract
    fixedMinimumShares = int(minShares * (10 ** 6))

    contract = web3_provider.eth.contract(address=marketMakerAddress, abi=fixed_product_market_maker_address_abi)
    trxHash = contract.functions.buy(approvedAmount, index, fixedMinimumShares).transact()
    web3_provider.eth.wait_for_transaction_receipt(trxHash)
    return trxHash
