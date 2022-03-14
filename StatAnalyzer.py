from CargoDistributionAnalysis import CargoDistributionAnalysis
from EventMethods import EventMethods
import pickle

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

        if(False): #run for all events in 2022
            allEvents = self.em.getAllMatchesFromYear(2022)
            print("Num events:" + str(len(allEvents)))
            allMatches = self.em.getAllMatchesFromEvents(allEvents)
            filteredEvents = self.em.filterEventsByMatches(allMatches)
            print(filteredEvents)
            for event in filteredEvents:
                temp = self.getDist.getDistFromMatchInfo(allMatches[event])
                print(event, temp, "\n")

        if(True):
            data = {}
            for year in range(2022, 2023):
                allEvents = self.em.getAllMatchesFromYear(year)
                tot = len(allEvents)
                print(tot)
                
                count = 0
                for event in allEvents:
                    key = event['key']
                    
                    temp = self.em.getMatchesDayFromEvent(key)
                    data[key] = temp
                    count = count + 1
                    print(key, temp, count/tot)

            print(data)
            with open('saveData2022', 'wb') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        if(False):
            allEvents = ["2014flpp"]
            tot = len(allEvents)
            print(tot)
            data = {}
            count = 0
            for event in allEvents:
                key = event
                
                temp = self.em.getMatchesDayFromEventNoPass(key)
                data[key] = temp
                count = count + 1
                print(key, temp, count/tot)

            print(data)