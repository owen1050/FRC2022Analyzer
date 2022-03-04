from CargoDistributionAnalysis import CargoDistributionAnalysis
from EventMethods import EventMethods
class StatAnalyzer:
    em = 0
    getDist = 0
    def test(self):
        self.em = EventMethods()
        self.getDist = CargoDistributionAnalysis()

        if(False):
            print(self.getDist.getDist("2022ispr"))

        if(False): #run for specific events
            filteredEvents = ['2022flwp', '2022ispr', '2022mndu', '2022mndu2', '2022week0']#self.em.filterEventsByMatches(allMatches)
            allMatches = self.em.getEventDataFromEvents(filteredEvents)

            for event in filteredEvents:
                temp = self.getDist.getDistFromMatchInfo(allMatches[event])
                print(event, temp)

        if(True): #run for all events in 2022
            allEvents = self.em.getAllMatchesFromYear(2022)
            allMatches = self.em.getAllMatchesFromEvents(allEvents)
            filteredEvents = self.em.filterEventsByMatches(allMatches)
            print(filteredEvents)
            for event in filteredEvents:
                temp = self.getDist.getDistFromMatchInfo(allMatches[event])
                print(event, temp)