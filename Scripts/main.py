import os
import time

tweet_searches = [
    'unemployment', 'amy coney barrett', 'cars', 'outdoors', 'food', 'football', 'climate change', 'animals', '2020',
    'covid19', 'facebook', 'ironman', 'giants', 'ronaldo', 'rudy', 'borat', 'guns', 'blm', 'surfing', 'tennis', 'amd',
    'esports', 'google', 'joker', 'vapes', 'alcohol', 'drugs', 'cartel', 'russia', 'north korea', 'dogs', 'cats',
    'computers', 'stocks', 'wallstreetbets', 'reddit', 'memes', 'emojis', 'college', 'liberals', 'conservatives',
    'usa', 'brexit', ''
]

for search in tweet_searches:
    os.system('python pull_tweets.py {}'.format(search))
    time.sleep(60 * 16)  # sleep 16 min for twitter refresh
