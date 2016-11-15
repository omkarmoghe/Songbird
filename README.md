# Songbird
Uses tweets from Twitter's trending topics to create music using Max MSP

Originally created for my cycle 3 project for PAT 201 at the Univeristy of Michigan.

## Building
You will need to create a Twitter app and use the dev console to generate auth keys/tokens for your app. https://apps.twitter.com/

Add the following keys to your `secrets.py` file:
```python
CONSUMER_KEY = 'your'
CONSUMER_SECRET = 'keys'
ACCESS_TOKEN = 'go'
ACCESS_TOKEN_SECRET = 'here'
```

Next run `python songbird_data_builder.py` to generate the data file, formatted as a Max `coll` object.

Finally, run the Max patch to play music!
