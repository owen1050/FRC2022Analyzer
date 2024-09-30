from EventMethods import EventMethods
import pickle
fileName = "allTeamsMatchesTog"

em = EventMethods()
outputData = {}

with open(fileName, 'rb') as handle:
    data = pickle.load(handle)


fileNameTest = "allTeamsTesting"


with open(fileNameTest, 'rb') as handle:
    allTeamData = pickle.load(handle)

teamList = []
for team in allTeamData:
    teamList.append(team['key'][3:])




for d in data:
	outputData[d] = data[d]

for team in teamList:
	team = int(team)
	if(team not in data):
		print("Downloading matches from team " + str(team))
		listAllEventCodesPerTeam = []
		allEventaData = em.getAllTeamEvents(team)
		for i in allEventaData:
			listAllEventCodesPerTeam.append(i['key'])

		allMatchesFromTeam = em.getTeamMatchesFromEvents(listAllEventCodesPerTeam, team)
		outputData[team] = allMatchesFromTeam
	else:
		print("Already downloaded matches from " + str(team))

	file = open(fileName, 'wb')
	pickle.dump(outputData, file)
	file.close()

