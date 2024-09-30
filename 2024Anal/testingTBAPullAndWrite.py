from EventMethods import EventMethods
from TeamMethods import TeamMethods
import pickle
fileName = "allTeamsTesting"

em = EventMethods()
tm = TeamMethods()
outputData = {}


with open(fileName, 'rb') as handle:
    data = pickle.load(handle)

outputData = tm.getAllTeams()


file = open(fileName, 'wb')
pickle.dump(outputData, file)
file.close()