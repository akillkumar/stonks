import csv
import json

# list of dictionaries, containing date and combined tweets
tweets = {}

with open ('Nike_tweets_2017_20.csv', encoding='utf-8') as fp:
    reader = csv.reader (fp)
    data = list (reader)

for tweet in data:
    if tweet[0] in tweets:
        tweets[tweet[0]] += " " + tweet[3]
    else:
        tweets[tweet[0]] = tweet[3]

with open ('results_2017_20.json', 'w') as fp:
    json.dump (tweets, fp, indent = 4)