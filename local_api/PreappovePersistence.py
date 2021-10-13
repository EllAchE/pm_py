class PreapprovePersistence:

    def __init__(self):
        self.w3Provider = None
        self.preapprovedAmount = None
        self.minShares = None

    def getPreapprovedAmount(self):
        if self.preapprovedAmount:
            return self.preapprovedAmount
        else:
            raise ValueError('Preapproved Amount is not set')

    def getWeb3Provider(self):
        if self.w3Provider:
            return self.w3Provider
        else:
            raise ValueError('Preapproved Amount is not set')

    def getA(self):
        if self.minShares:
            return self.minShares
        else:
            raise ValueError('Minimum shares not set')

    def setPreapprovedAmount(self, preapprovedAmount):
        self.preapprovedAmount = preapprovedAmount
        self.minShares = preapprovedAmount / 0.977 # todo make this something that can be passed via endpoint

    def setWeb3Provider(self, w3Provider):
        self.w3Provider = w3Provider
