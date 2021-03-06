from polymarket import initialize_identity, load_evm_abi
from polymarket.amm.maths import calc_sell_amount_in_collateral
from polymarket.utils import conditional_token_approve_for_all, get_pool_balances

# todo add error checking
from local_api.endpoint_methods.custom_utils import EARLY_EXIT_STRING, createSellSharesReturnJson, SUCCESS_RESPONSE_STRING


def sellShares(conditionId, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas):
    print("received args")
    print("conditionId", conditionId)
    print("mmAddress", mmAddress)
    print("numberOfShares", numberOfShares)
    print("outcomeIndex", outcomeIndex)
    print("numberOfOutcomes", numberOfOutcomes)
    print("slippage", slippage)
    print("fee", fee)
    print("gas", gas)

    try:
        outcomeIndex = int(outcomeIndex)
        numberOfShares = float(numberOfShares)
        gas = int(gas)
    except Exception as e:
        return createSellSharesReturnJson(e, mmAddress, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage, fee, gas, EARLY_EXIT_STRING)


    fixed_product_market_maker_address_abi = load_evm_abi('FixedProductMarketMaker.json')

    fixed_share_count = int(numberOfShares * (10**6))
    w3Provider = initialize_identity(gas)

    conditional_token_approve_for_all(w3Provider, mmAddress, True)
    contract = w3Provider.eth.contract(address=mmAddress, abi=fixed_product_market_maker_address_abi)
    # fee = float(int(market_json['fee']) / (10 ** 18)) # needs to be referenced from marketJson

    pool_balances = get_pool_balances(w3Provider, mmAddress, conditionId, numberOfOutcomes)
    sell_amount_in_usdc = calc_sell_amount_in_collateral(fixed_share_count, outcomeIndex, pool_balances, fee)

    fixed_return_amount = int(round(float(sell_amount_in_usdc)))

    slippage_fixed_share_count = int(fixed_share_count * (1 + (slippage/100)))

    trx_hash = contract.functions.sell(fixed_return_amount, outcomeIndex, slippage_fixed_share_count).transact()
    w3Provider.eth.wait_for_transaction_receipt(trx_hash)

    conditional_token_approve_for_all(w3Provider, mmAddress, False)

    return createSellSharesReturnJson(SUCCESS_RESPONSE_STRING, mmAddress, mmAddress, numberOfShares, outcomeIndex, numberOfOutcomes, slippage,
                                      fee, gas, trx_hash)
# todo fix this to use slug as the base does in an alternate. Time will be lost in the request/response but probably negligible