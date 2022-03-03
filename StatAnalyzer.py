from CargoDistributionAnalysis import CargoDistributionAnalysis

class StatAnalyzer:

    def test(self):
        print(self.getCargoDropRateDistributionFromEvent("2022week0"))

    def getCargoDropRateDistributionFromEvent(self, eventKey):
        getDist = CargoDistributionAnalysis()
        data = getDist.getDist(eventKey)
        return data

    def getAllEvents(self):
        pass
