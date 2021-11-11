from local_api.PreapprovedMarket import PreapprovedMarket


class PreapprovePersistence:
    def __init__(self):
        self.w3Provider = None
        self.preapprovedAmounts = {}

    def getWeb3Provider(self):
        if self.w3Provider:
            return self.w3Provider
        else:
            print('Amount is not set')
            return 'Amount is not set' # todo should not throw an error

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
        except Exception as e:
            print("preapproved amount not set for mmAddress {}, returning None.\n Exception read {}".format(mmAddress, e))
            return None
