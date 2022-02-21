import tbapy
itemKeys = ["autoCargoLowerBlue",'autoCargoLowerFar','autoCargoLowerNear','autoCargoLowerRed','autoCargoUpperBlue','autoCargoUpperFar','autoCargoUpperNear','autoCargoUpperRed','teleopCargoLowerBlue','teleopCargoLowerFar','teleopCargoLowerNear','teleopCargoLowerRed','teleopCargoUpperBlue','teleopCargoUpperFar','teleopCargoUpperNear','teleopCargoUpperRed']
items = {}
for item in itemKeys:
    items[item] = 0

tba = tbapy.TBA('')

matches = tba.event_matches("2022week0")
for match in matches:
    r = match["score_breakdown"]["red"]
    b = match["score_breakdown"]["blue"]
    for item in itemKeys:
        items[item] = items[item] + r[item] + b[item]

print(items)

