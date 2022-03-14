from CargoDistributionAnalysis import CargoDistributionAnalysis
from EventMethods import EventMethods
import pickle

class StatAnalyzer:
    em = 0
    getDist = 0
    itemKeys = ["autoCargoLowerBlue",'autoCargoLowerFar','autoCargoLowerNear','autoCargoLowerRed','autoCargoUpperBlue','autoCargoUpperFar','autoCargoUpperNear','autoCargoUpperRed','teleopCargoLowerBlue','teleopCargoLowerFar','teleopCargoLowerNear','teleopCargoLowerRed','teleopCargoUpperBlue','teleopCargoUpperFar','teleopCargoUpperNear','teleopCargoUpperRed']
    items = {}

    def test(self):
        self.em = EventMethods()
        self.getDist = CargoDistributionAnalysis()

        if(False):
            filteredEvents = ['2022njbri']#self.em.filterEventsByMatches(allMatches)
            allMatches = self.em.getEventDataFromEvents(filteredEvents)
            print(allMatches['2022njbri'][45])



        if(False): #run for specific events
            filteredEvents = ['2022njbri']#self.em.filterEventsByMatches(allMatches)
            allMatches = self.em.getEventDataFromEvents(filteredEvents)

            for event in filteredEvents:
                temp = self.getDist.getDistFromMatchInfo(allMatches[event])
                print(temp)

        if(False): #run for all events in 2022
            allEvents = self.em.getAllMatchesFromYear(2022)
            print("Num events:" + str(len(allEvents)))
            allMatches = self.em.getAllMatchesFromEvents(allEvents)
            print("Num events w/ matches:" + str(len(allMatches)))
            filteredEvents = self.em.filterEventsByMatches(allMatches)
            print(filteredEvents)
            for item in self.itemKeys:
                self.items[item] = 0
            count = 0
            for event in filteredEvents:
                temp = self.getDist.getDistFromMatchInfo(allMatches[event])
                print(event, temp, "\n")

        if(True):
            data = {}
            for year in range(2008, 2023):
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
            with open('saveData', 'wb') as handle:
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
