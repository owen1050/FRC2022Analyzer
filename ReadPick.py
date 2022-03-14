import pickle

with open('saveData', 'rb') as handle:
    data = pickle.load(handle)

with open('saveData2022', 'rb') as handle:
    data2022 = pickle.load(handle)

for d in data2022:
    data[d] = data2022[d]

print(data)
m = 0
newData = {}
for event in data:
    for day in data[event]:


        t = data[event][day]
        newData[event+":"+str(day)] = t
        if t > m:
            m = t
            print(event, day, t)

sortedEvents = {}
sortedEvents = sorted(newData, key = newData.get)
newSorted = {}
print(sortedEvents)
for w in sortedEvents:
    newSorted[w] = newData[w]

for i in newSorted:
    print(i, newSorted[i])