from polymarket.utils import approve_erc20

from polymarket import initialize_identity

from local_api.endpoint_methods.utils import createPreapprovalReturnJson, SUCCESS_RESPONSE_STRING


def preapproveAmount(amount, gas, mmAddress, persistObj):
    print('amount', amount)
    print('gas', gas)
    print('mmAddress', mmAddress)

    try:
        minShares = float(amount) / 0.977
        gas = int(gas)

        print('initializing identity')
        w3 = initialize_identity(gas)

        print('setting values on persist obj')
        persistObj.setWeb3Provider(w3)
        approvedAmount = preapprove(w3, mmAddress, amount), w3
        persistObj.addPreapproval(mmAddress, minShares, approvedAmount)
        print('set values on persist obj')

        return createPreapprovalReturnJson(SUCCESS_RESPONSE_STRING, amount, gas, mmAddress, "no trx hash for preapproval")
    except Exception as e:
        print('error in preapprove')
        return createPreapprovalReturnJson(e, amount, gas, mmAddress, "no trx hash for preapproval")

def preapprove(web3_provider, market_maker_address, amount):
    return approve_erc20(web3_provider, market_maker_address, amount)