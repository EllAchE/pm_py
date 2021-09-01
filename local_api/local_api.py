from flask import Flask

from polymarket import initialize_identity, buy

app = Flask(__name__)

# 0x18f541b0844BEB2517A7B825a95402227536234b
# Secretary firing by october test market address

# Test trigger url http://localhost:5000/polybuy/0x18f541b0844BEB2517A7B825a95402227536234b/0.5/1/0.52/15

@app.route('/polybuy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
def buyOrder(mmAddress, amount, outcomeIndex, minShares, gas):
    # Pring arguments to py console. Likely unseen
    print("mmAddress", mmAddress)
    print("amount", amount)
    print("outcomeIndex", outcomeIndex)
    print("minShares", minShares)
    print("gas", gas)

    # Actual purchase logic
    w3 = initialize_identity(gas)
    try :
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print(trx_hash)

    print('hash made', trx_hash)

    return {
        "mmAddress": mmAddress,
        "amount": amount,
        "outcomeIndex": outcomeIndex,
        "minShares": minShares,
        "gas": gas,
        "transactionHash": trx_hash
    }

app.run()