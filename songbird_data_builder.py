from TwitterSearch import *
from secrets import *

tso = TwitterSearchOrder() # create a TwitterSearchOrder object
tso.set_keywords(['#TuesdayMotivation']) # let's define all words we would like to have a look for
tso.set_language('en') # we want to see German tweets only
tso.set_include_entities(False) # and don't give us all those entity information

search = TwitterSearch(consumer_key=CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
    )

for tweet in search.search_tweets_iterable(tso):
    handle = tweet['user']['screen_name'].encode('utf-8')
    content = tweet['text'].encode('utf-8')
    print('@{} tweeted: {}'.format(handle.encode('utf-8'), len(content)))
