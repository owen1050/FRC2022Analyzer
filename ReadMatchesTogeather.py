import pickle

with open('allTeamsAr2024rr', 'rb') as handle:
    data = pickle.load(handle)

globalTPW = {}
globalTPA = {}

teamsG = ['11', '25','254', '303','316','369','555','714','1279','1629','1676', '1923', '2577','3142','3637','4012','4361','4653','6897','7045','7587','8075','8117','8513', '8588','8630','8714','9015']


for team in data:
    teamsPlayedWith = {}
    teamsPlayedAgainst = {}
    
    for event in data[team]:

        thisEvent = data[team][event]
        for match in thisEvent:
            red = match['alliances']['red']['team_keys']
            blue = match['alliances']['blue']['team_keys']
            tmp = []
            for teamCode in red:
                try:
                    tmp.append(int(teamCode[3:]))
                except:
                    pass
            red = tmp

            tmp = []
            for teamCode in blue:
                try:
                    tmp.append(int(teamCode[3:]))
                except:
                    pass
            blue = tmp
            if(team in red):
                for redTeam in red:
                    teamsPlayedWith[redTeam] = teamsPlayedWith.get(redTeam, 0) + 1
                for blueTeam in blue:
                    teamsPlayedAgainst[blueTeam] = teamsPlayedAgainst.get(blueTeam, 0) + 1
            if(team in blue):
                for redTeam in red:
                    teamsPlayedAgainst[redTeam] = teamsPlayedAgainst.get(redTeam, 0) + 1
                for blueTeam in blue:
                    teamsPlayedWith[blueTeam] = teamsPlayedWith.get(blueTeam, 0) + 1

    globalTPW[team] = teamsPlayedWith
    globalTPA[team] = teamsPlayedAgainst

print("", end= "\t")
for team in teamsG:
    print(team, "\t", end = "")

for teama in teamsG:
    team1 = int(teama)
    print("")
    print(teama, end = "\t")
    for teamb in teamsG:
        team2 = int(teamb)
        print(globalTPW[team1].get(team2,0), end = "\t")





