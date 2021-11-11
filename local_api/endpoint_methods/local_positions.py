from polymarket import list_positions, initialize_identity


def localListPositions():
    print("attempting to list positions")
    w3 = initialize_identity(2) # hardcoded to 2 gwei
    print("initialized identity")
    list_positions(w3, w3.eth.default_account)