from polymarket import initialize_identity, load_evm_abi, sell_shares
from polymarket.amm.maths import calc_sell_amount_in_collateral
from polymarket.utils import conditional_token_approve_for_all, get_pool_balances

def sellShares(slug, outcomeIndex, numberOfShares, slippage, gas):
    w3Provider = initialize_identity(gas)
    trxHash = sell_shares(w3Provider, slug, outcomeIndex, numberOfShares, slippage)
    return trxHash