from local_api.PreapprovedMarket import PreapprovedMarket


class PreapprovePersistence:
    def __init__(self):
        self.w3Provider = None
        self.preapprovedAmounts = {}
        self.minShares = None

    def getWeb3Provider(self):
        if self.w3Provider:
            return self.w3Provider
        else:
            raise ValueError('Preapproved Amount is not set')

    def setWeb3Provider(self, w3Provider):
        if not self.w3Provider:
            self.w3Provider = w3Provider
        else:
            print("w3 provider already set") # todo need to validate if the same 23 provier can be used for multiple transactions

    def addPreapproval(self, mmAddress, minShares, preapprovedAmount):
        self.preapprovedAmounts[mmAddress] = PreapprovedMarket(mmAddress, minShares, preapprovedAmount)

    def getPreapproval(self, mmAddress):
        try:
            return self.preapprovedAmounts[mmAddress]
        except:
            print("preapproved amount not set for mmAddress {}, returning None".format(mmAddress))
            return None
