import tbapy
from TBAGetter import TBAGetter

class EventMethods:

    tba = 0

    def __init__(self):
        self.tba = TBAGetter().getTBA()

    def getAllEventsFromYear(self, year):
        return self.tba.events(year)

    def getAllMatchesFromYear(self, year):
        events = self.getAllEventsFromYear(year)
        return events

    def getAllMatchesFromEvents(self, events):
        ret = {}
        for event in events:
            tempMatches = self.tba.event_matches(event['key'])
            ret[event['key']] = tempMatches
        return ret

    def filterEventsByMatches(self, events):
        ret = []
        for event in events:
            if len(events[event]) > 0:
                ret.append(event)
        return ret

    def getAllEventsFromYearWithMatches(self, year):
        events = self.getAllEventsFromYear(year)
        return self.filterEventsByMatches(events)

    def getEventDataFromEvents(self, events):
        ret = {}
        for event in events:
            tempMatches = self.tba.event_matches(event)
            ret[event] = tempMatches
        return ret
