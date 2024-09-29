from EventMethods import EventMethods
import pickle
fileName = "allTeamsAr2024rr"

em = EventMethods()
outputData = {}

with open('allTeamsAr2024rr', 'rb') as handle:
    data = pickle.load(handle)

teams = ['11', '25','254', '303','316','369','555','714','1279','1629','1676', '1923', '2577','3142','3637','4012','4361','4653','6897','7045','7587','8075','8117','8513', '8588','8630','8714','9015']

for d in data:
	outputData[d] = data[d]

for team in teams:
	team = int(team)
	if(team not in data):
		print("Downloading matches from team" + str(team))
		listAllEventCodesPerTeam = []
		allEventaData = em.getAllTeamEvents(team)
		for i in allEventaData:
			listAllEventCodesPerTeam.append(i['key'])

		allMatchesFromTeam = em.getTeamMatchesFromEvents(listAllEventCodesPerTeam, team)
		outputData[team] = allMatchesFromTeam
	else:
		print("Already downloaded matches from" + str(team))
file = open(fileName, 'wb')
pickle.dump(outputData, file)