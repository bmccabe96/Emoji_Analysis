import os
import time

# Note, keeping track of all the searches I've done over the days I gathered data
# FYI -- Every 4 search topics takes a little over an hour to complete
tweet_searches = [
    # 'unemployment', 'amy coney barrett', 'cars', 'outdoors', 'food', 'football', 'climate change', 'animals', '2020',
    # 'covid19', 'facebook', 'ironman', 'giants', 'ronaldo', 'rudy', 'borat', 'guns', 'blm', 'surfing', 'tennis', 'amd',
    # 'esports', 'google', 'joker', 'vapes', 'alcohol', 'drugs', 'cartel', 'russia', 'north korea', 'dogs', 'cats',
    # 'computers', 'stocks', 'wallstreetbets', 'reddit', 'memes', 'emojis', 'college', 'liberals', 'conservatives',
    # 'usa', 'brexit'

    # 'dez bryant', 'cyberpunk', 'fires', 'nascar', 'starlink', 'liverpool', 'msft', 'harry styles', 'seahawks',
    # 'music', 'vote'
    
    # this round of data gathering was shooting for some more negative sentiments...
    'coronavirus', 'war', 'racism', 'cancer', 'sad', 'angry', 'fear', 'scary', 'trump', '2020', 'global warming',
    'fires', 'evil', 'guns', 'death'
]

for search in tweet_searches:
    os.system('python pull_tweets.py {}'.format(search))
    time.sleep(60 * 16)  # sleep 16 min for twitter refresh
