from twython import Twython
import twython
import sys
import mysql.connector
import config
import time


def create_twitter(APP_KEY=config.api_key, APP_SECRET=config.api_secret_key):
    """

    :param APP_KEY: app key, default to value set in config file
    :param APP_SECRET: app secret, default to value set in config file
    :return: twython object
    """
    twit = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twit.obtain_access_token()
    return Twython(APP_KEY, access_token=ACCESS_TOKEN)


def store_tweet(tweet, conn, curs):
    """
    This will take a tweet and store it in mysql
    :param tweet: a tweet from twython
    :param conn: database connection
    :param curs: cursor for database
    :return: none
    """
    to_add = [tweet['text']]
    insert_query = """
                    INSERT IGNORE INTO Election_Tweets 
                    VALUES (DEFAULT, %s)
                    """
    curs.execute(insert_query, to_add)
    conn.commit()


def iterate_tweets(gnrtr, conn, curs):
    counter = 1
    for result in gnrtr:
        try:
            store_tweet(result, conn, curs)
            if counter % 25 == 0:
                print(f"Added {counter} tweet to database")
            counter += 1

        except twython.exceptions.TwythonRateLimitError as error:
            print("Ran into rate limit, continuing after 15 minute sleep")

        except twython.exceptions.TwythonError as error:
            print("Servers overloaded, continueing after 15 minute sleep")


# Command level argument to determine topic of twitter search
topic = sys.argv[1]
# Create twitter object
twitter = create_twitter()

try:
    # Connect to the database
    connection = mysql.connector.connect(host=config.host, user=config.user, port=config.port, password=config.password,
                                         database=config.database, auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    use_query = "USE Twitter"
    cursor.execute(use_query)

    results = twitter.cursor(twitter.search, q=topic, lang='en')  # generator object of tweets

    try:
        iterate_tweets(results, connection, cursor)

    except twython.exceptions.TwythonRateLimitError as error:
        print("Ran into rate error, continuing after 15 minute sleep")

    except RuntimeError as error:
        print("Runtime error...")


except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
