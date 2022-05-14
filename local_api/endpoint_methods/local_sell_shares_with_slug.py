from polymarket import initialize_identity, sell_shares
from local_api.endpoint_methods.custom_utils import createSlugSellReturnJson

def sellShares(slug, outcomeLabel, numberOfShares, slippage, gas):
    w3Provider = initialize_identity(gas)
    trxHash = sell_shares(w3Provider, slug, outcomeLabel, numberOfShares, slippage)
    return createSlugSellReturnJson(SUCCESS_RESPONSE_STRING, slug, outcomeLabel, numberOfShares, slippage, gas, trxHash)