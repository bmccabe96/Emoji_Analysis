import os
import time

# Note, keeping track of all the searches I've done over the days I gathered data
# FYI -- Every 4 search topics takes a little over an hour to complete
tweet_searches = [
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',
    'election', 'trump', 'biden', 'vote', 'president','election', 'trump', 'biden', 'vote', 'president',


]

for search in tweet_searches:
    os.system('python pull_tweets.py {}'.format(search))
    time.sleep(60 * 16)  # sleep 16 min for twitter refresh
