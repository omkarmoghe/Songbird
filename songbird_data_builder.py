import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()  # generally not a good idea...

from TwitterSearch import *
from secrets import *


print('Building search...')
tso = TwitterSearchOrder() # create a TwitterSearchOrder object
tso.set_keywords(['#TuesdayMotivation']) # let's define all words we would like to have a look for
tso.set_language('en') # we want to see German tweets only
tso.set_include_entities(False) # and don't give us all those entity information
tso.set_count(100)

search = TwitterSearch(consumer_key=CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
    )

print('Writing file...')
with open('tweet_sounds.txt', 'w') as file:
    index = 0;
    for tweet in search.search_tweets_iterable(tso):
        handle = tweet['user']['screen_name'].encode('utf-8')
        content = tweet['text'].encode('utf-8')

        file.write('{}, {} {};\n'.format(index, len(handle), len(content)))
        
        index += 1
        if index > 300:
            break

print('Done! Created file \'tweet_sounds.txt\'')
