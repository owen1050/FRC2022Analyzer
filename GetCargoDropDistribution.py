import tbapy
itemKeys = ["autoCargoLowerBlue",'autoCargoLowerFar','autoCargoLowerNear','autoCargoLowerRed','autoCargoUpperBlue','autoCargoUpperFar','autoCargoUpperNear','autoCargoUpperRed','teleopCargoLowerBlue','teleopCargoLowerFar','teleopCargoLowerNear','teleopCargoLowerRed','teleopCargoUpperBlue','teleopCargoUpperFar','teleopCargoUpperNear','teleopCargoUpperRed']
items = {}
timeAgItems = {}

for item in itemKeys:
    items[item] = 0

for item in itemKeys:
    i0 = item.find("C")
    newItem = item[i0:]
    timeAgItems[newItem] = 0

f = open("TOKEN", 'r')
tok = f.read()
f.close()
tba = tbapy.TBA(tok)


matches = tba.event_matches("2022week0")
for match in matches:
    r = match["score_breakdown"]["red"]
    b = match["score_breakdown"]["blue"]
    for item in itemKeys:
        items[item] = items[item] + r[item] + b[item]
        i0 = item.find("C")
        newItem = item[i0:]
        timeAgItems[newItem] = timeAgItems[newItem] +  r[item] + b[item]

total = 0
lowerTotal = 0
upperTotal = 0
for i in timeAgItems:
    total = total + timeAgItems[i]
    if(i.find("Lower") >=0 ):
        lowerTotal = lowerTotal + timeAgItems[i]

upperTotal = total - lowerTotal

timeAgDistLower = {}
timeAgDistUpper = {}
for i in timeAgItems:
    if(i.find("Lower") >=0 ):
        timeAgDistLower[i] = timeAgItems[i] / lowerTotal
    else:
        timeAgDistUpper[i] = timeAgItems[i] / upperTotal

for i in timeAgDistUpper:
    print(i, end = ":")
    print(round(timeAgDistUpper[i] * 100,2), end="%\t")
print()
for i in timeAgDistLower:
    print(i, end = ":")
    print(round(timeAgDistLower[i] * 100,2), end="%\t")
print()
print(lowerTotal, upperTotal, total)