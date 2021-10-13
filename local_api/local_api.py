from flask import Flask

from polymarket import initialize_identity, buy

app = Flask(__name__)

# 0x18f541b0844BEB2517A7B825a95402227536234b
# Secretary firing by october test market address

# Test trigger url http://127.0.0.1:5000/polybuy/0x18f541b0844BEB2517A7B825a95402227536234b/0.5/1/0.52/1

@app.route('/polybuy/<mmAddress>/<amount>/<outcomeIndex>/<minShares>/<gas>')
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
    except Exception as e:
        return createReturnJson(e, mmAddress, amount, outcomeIndex, minShares, gas, "Execution exited early")

    # Actual purchase logic
    w3 = initialize_identity(gas)
    try :
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print('hash made', str(trx_hash))

    return createReturnJson("200 OK", mmAddress, amount, outcomeIndex, minShares, gas, trx_hash)

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

app.run()