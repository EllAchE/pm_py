from flask import Flask

from polymarket import initialize_identity, buy

app = Flask(__name__)

# 0x18f541b0844BEB2517A7B825a95402227536234b
# Secretary firing by october test market address

@app.route('/polybuy/<mmAddress>/<int:amount>/<int:outcomeIndex>/<float:minShares>/<int:gas>')
def buyOrder(mmAddress, amount, outcomeIndex, minShares, gas):
    print("inside help")
    w3 = initialize_identity(gas)
    print('initialized')
    try :
        trx_hash = buy(w3, mmAddress, amount, outcomeIndex, minShares)
    except Exception as err:
        trx_hash = err
    print(trx_hash)
    print('hash made')
    return trx_hash
app.run()