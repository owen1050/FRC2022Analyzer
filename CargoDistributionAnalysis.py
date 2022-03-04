import tbapy
from TBAGetter import TBAGetter
itemKeys = ["autoCargoLowerBlue",'autoCargoLowerFar','autoCargoLowerNear','autoCargoLowerRed','autoCargoUpperBlue','autoCargoUpperFar','autoCargoUpperNear','autoCargoUpperRed','teleopCargoLowerBlue','teleopCargoLowerFar','teleopCargoLowerNear','teleopCargoLowerRed','teleopCargoUpperBlue','teleopCargoUpperFar','teleopCargoUpperNear','teleopCargoUpperRed']
items = {}
timeAgItems = {}

class CargoDistributionAnalysis:

    def getDistFromMatchInfo(self, eventData):
        for item in itemKeys:
            items[item] = 0

        for item in itemKeys:
            i0 = item.find("C")
            newItem = item[i0:]
            timeAgItems[newItem] = 0

        try:
            eventData[0]["score_breakdown"]["red"]
        except:
            return ({},{})

        for match in eventData:
            try:
                r = match["score_breakdown"]["red"]
                b = match["score_breakdown"]["blue"]
                for item in itemKeys:
                    items[item] = items[item] + r[item] + b[item]
                    i0 = item.find("C")
                    newItem = item[i0:]
                    timeAgItems[newItem] = timeAgItems[newItem] +  r[item] + b[item]
            except:
                print("error on line 25 of CargoDistributionAnalysis")


        total = 0
        lowerTotal = 0
        upperTotal = 0
        for i in timeAgItems:
            total = total + timeAgItems[i]
            if(i.find("Lower") >=0 ):
                lowerTotal = lowerTotal + timeAgItems[i]

        upperTotal = total - lowerTotal
        if(total == 0):
            return ({},{})

        timeAgDistLower = {}
        timeAgDistUpper = {}
        for i in timeAgItems:
            if(i.find("Lower") >=0 ):
                timeAgDistLower[i] = timeAgItems[i] / lowerTotal
            else:
                timeAgDistUpper[i] = timeAgItems[i] / upperTotal

        return (timeAgDistLower, timeAgDistUpper)

    def getDist(self, eventKey):

        for item in itemKeys:
            items[item] = 0

        for item in itemKeys:
            i0 = item.find("C")
            newItem = item[i0:]
            timeAgItems[newItem] = 0

        tba = TBAGetter().getTBA()
        matches = tba.event_matches(eventKey)
        return self.getDistFromMatchInfo(matches)

    def format(self):
        for i in timeAgDistUpper:
            print(i, end = ":")
            print(round(timeAgDistUpper[i] * 100,2), end="%\t")
        print()
        for i in timeAgDistLower:
            print(i, end = ":")
            print(round(timeAgDistLower[i] * 100,2), end="%\t")
        print()
        print(lowerTotal, upperTotal, total)