from CargoDistributionAnalysis import CargoDistributionAnalysis
from EventMethods import EventMethods
class StatAnalyzer:
    em = 0
    getDist = 0
    def test(self):
        self.em = EventMethods()
        self.getDist = CargoDistributionAnalysis()

        if(True):
            print(self.getDist.getDist("2022ispr"))

        if(False):
            allEvents = self.em.getAllMatchesFromYear(2022)
            allMatches = self.em.getAllMatchesFromEvents(allEvents)
            filteredEvents = self.em.filterEventsByMatches(allMatches)
            print(filteredEvents)

