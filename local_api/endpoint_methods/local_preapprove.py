from polymarket.utils import approve_erc20

from polymarket import initialize_identity

def preapproveAmount(amount, gas, mmAddress, persistObj):
    w3 = initialize_identity(gas)
    persistObj.setWeb3Provider(w3)
    approvedAmount = preapprove(w3, mmAddress, amount), w3
    persistObj.setPreapprovedAmount(approvedAmount, mmAddress)
    return approvedAmount

def preapprove(web3_provider, market_maker_address, amount):
    return approve_erc20(web3_provider, market_maker_address, amount)