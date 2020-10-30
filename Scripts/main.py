import os
import time

# Note, keeping track of all the searches I've done over the days I gathered data
# FYI -- Every 4 search topics takes a little over an hour to complete
tweet_searches = [
    # 'unemployment', 'amy coney barrett', 'cars', 'outdoors', 'food', 'football', 'climate change', 'animals', '2020',
    # 'covid19', 'facebook', 'ironman', 'giants', 'ronaldo', 'rudy', 'borat', 'guns', 'blm', 'surfing', 'tennis', 'amd',
    # 'esports', 'google', 'joker', 'vapes', 'alcohol', 'drugs', 'cartel', 'russia', 'north korea', 'dogs', 'cats',
    # 'computers', 'stocks', 'wallstreetbets', 'reddit', 'memes', 'emojis', 'college', 'liberals', 'conservatives',
    # 'usa', 'brexit', 'global warming',# 'fires', 'evil', 'guns', 'death', 'news' # 'bluelight',
    # 'dez bryant', 'cyberpunk', 'fires', 'nascar', 'starlink', 'liverpool', 'msft', 'harry styles', 'seahawks',
    # 'music', 'vote' # 'coronavirus', 'war', 'racism', 'cancer', 'sad', 'angry', 'fear', 'scary', 'trump', '2020',
    # 'sweater weather', 'cold', 'philadelphia', 'portland', 'black lives matter', 'all lives matter', 'blue lives matter',
    # 'police', 'capitalism', 'wisconsin', 'abuse', 'cheating', 'putin', 'riots', 'burning', 'iphone', 'white', 'gyms',
    # 'halloween', 'costumes', 'vampires', 'netflix', 'fungi', 'bezos', 'amazon', 'privacy', 'social dilemma',
    # 'congress', 'justice', 'data', 'Trending', 'Scary', 'Horror', 'Gangs', 'Blood', 'sickness', 'bullying',
    # 'shooting', 'college', 'censor', 'data', 'senator', 'president', 'racism'

    'news', 'usa', 'fun', 'video', 'youtube', 'hulu', 'invest', 'music', 'rap', 'comedy', 'reviews', 'water',
    'winter', 'beach', 'china', 'asia', 'natural gas', 'gem', 'moon', 'space', 'monster', 'sufing', 'cheese', 'europe',
    'france', 

    #'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    #'v', 'w', 'x', 'y', 'z'
]

for search in tweet_searches:
    os.system('python pull_tweets.py {}'.format(search))
    time.sleep(60 * 16)  # sleep 16 min for twitter refresh
