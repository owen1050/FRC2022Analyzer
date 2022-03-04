from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Today's Wordle"]
pytrends.build_payload(kw_list, cat=0, timeframe='now 1-d', geo='', gprop='')
related_searches = list(pytrends.related_queries()['Todays Wordle']['rising']['query'])

word_frequency = {}
for search in related_searches:
    words = search.split(' ')
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    
sorted_words = sorted(word_frequency.items(), reverse=True, key=lambda item: item[1])
filtered_words = [word[0] for word in sorted_words if len(word[0]) == 5 and word[0] not in ['words', 'start', 'terms']]

print('results (in order of most to least likely): ')
for (i, word) in enumerate(filtered_words[:3]):
    print('{0}. {1}'.format(i+1, word))