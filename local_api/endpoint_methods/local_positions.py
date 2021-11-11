from polymarket import list_positions, initialize_identity


def localListPositions():
    print("attempting to list positions")
    w3 = initialize_identity(1)
    print("initialized identity")
    list_positions(w3, w3.eth.default_account)
    print("should've listed positions")