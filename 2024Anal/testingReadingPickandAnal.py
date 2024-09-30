import pickle
fileName = "allTeamsTesting"


with open(fileName, 'rb') as handle:
    allTeamData = pickle.load(handle)

teamList = []
for team in allTeamData:
    teamList.append(team['key'][3:])

