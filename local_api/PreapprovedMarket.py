class PreapprovedMarket:
    def __init__(self, mmAddress, minShares, preapprovedAmount):
        self.preapprovedAmount = preapprovedAmount
        self.minShares = minShares
        self.mmAddress = mmAddress

    def getA(self):
        if self.minShares:
            return self.minShares
        else:
            raise ValueError('Minimum shares not set')

    def getPreapprovedAmount(self):
        if self.preapprovedAmount:
            return self.preapprovedAmount
        else:
            raise ValueError('Preapproved Amount is not set')