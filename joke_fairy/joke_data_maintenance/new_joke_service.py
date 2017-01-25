import os
from collections import namedtuple
from datetime import datetime
from pathlib import Path

import praw
from tinydb import TinyDB, Query

from reddit_login.passwords import CLIENT_ID, CLIENT_SECRET, USER_AGENT

Day = namedtuple('Day', 'start, end')
Joke = Query()

SUBREDDITS = ['jokes', 'dadjokes', 'cleanjokes', 'dirtyjokes']
DAYSTOGET = 3

def main():

    db = open_jokes_database()
    reddit = connect_to_reddit()
    update_database(db, reddit)


def open_jokes_database():
    directory = Path(os.path.abspath(os.path.dirname(__file__)))
    jokesdb_path = os.path.join(str(directory.parent), 'db', 'jokesdb.json')
    return TinyDB(jokesdb_path)


def update_database(db, reddit):

    for subreddit in SUBREDDITS:

        now = one_day_timestamps()

        for _ in range(DAYSTOGET):
            now_jokes = reddit.subreddit(subreddit).submissions(now.start, now.end)
            print('Found {} jokes on {}.'.format(subreddit, datetime.fromtimestamp(now.end).date()))
            n = 0
            try:
                for joke in now_jokes:
                    if joke.score < 10:
                        pass
                    elif not db.search(Joke.id == joke.id):
                        n += 1
                        db.insert({'id': str(joke.id), 'title': joke.title, 'content': joke.selftext,
                                   'score': joke.score, 'subreddit': str(joke.subreddit)})
                    else:
                        print('Joke {} is already in here.'.format(joke.id))

            except Exception as e:
                print('Issue with jokes on {}. {}'.format(datetime.fromtimestamp(now.end).date(), e))

            print("Added {} jokes from {}.".format(n, datetime.fromtimestamp(now.end).date()))

            now = one_day_timestamps(now.start)


def one_day_timestamps(end = datetime.timestamp(datetime.today())):
    # Returns tuple of timestamps for beg and end of a day's period
    oneday = 24*60*60
    start = end - oneday
    return Day(start, end)


def connect_to_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)

    return reddit

if __name__ == '__main__':
    main()