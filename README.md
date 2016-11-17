# Songbird
Uses tweets from Twitter's trending topics to create music using Max MSP

Originally created for my cycle 3 project for PAT 201 at the Univeristy of Michigan.

## Building
You will need to create a Twitter app and use the dev console to generate auth keys/tokens for your app. https://apps.twitter.com/

Next, create a file called `secrets.py` and add the following keys to the file:
```python
CONSUMER_KEY = 'your'
CONSUMER_SECRET = 'keys'
ACCESS_TOKEN = 'go'
ACCESS_TOKEN_SECRET = 'here'
```

Now you can run `python songbird.py filename [keywords...]` to generate the data file, formatted as a Max `coll` object.

For example, `python songbird.py sick_bands.txt #SickBands` would generate a file called `sick_bands.txt` with the corresponding MIDI data based on tweets from the "#SickBands" trending topic.

Max coll objects are formatted as follows:
```
index, value1 value2;
```
Internally, `value1` and `value2` are being scaled and used as pitch and velocity respectively.

Finally, run the Max patch to play music!
