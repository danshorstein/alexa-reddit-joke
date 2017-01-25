import os
import random
from collections import namedtuple
from datetime import datetime

import praw
from tinydb import TinyDB, Query

from joke_fairy.joke_data_maintenance.reddit_login.passwords import CLIENT_ID, CLIENT_SECRET, USER_AGENT

# This file downloads a large amount of jokes from reddit, and stores them in a joke JSON file.
# If the JSON file already exists, this will compare to what's in there and only add jokes if they
# Are not in there yet. It will keep the

Day = namedtuple('Day', 'start, end')
Joke = Query()

"""Save for later:
    Joke = Query()    Joke = Query()
    print(len(data.search(Joke['content'].search(r'sex'))))
"""

SUBREDDIT = 'dadjokes'
DAYSTOGET = 300

def main():

    db = open_jokes_database()
    reddit = connect_to_reddit()
    make_new_database(db, reddit)


def open_jokes_database():
    directory = os.path.abspath(os.path.dirname(__file__))
    jokesdb_path = os.path.join(directory, 'jokesdb.json')
    return TinyDB(jokesdb_path)


def add_joke_to_db(db, joke_id, reddit):
    if not db.search(Joke['id'].search(str(joke_id))):
        joke = reddit.submission(id=joke_id)
        db.insert({'id': str(joke.id), 'title': joke.title, 'content': joke.selftext, 'score': joke.score})


def make_new_database(db, reddit):
    # This should only be run to initialize the database the first time. It pulls all the hot, top, and last two
    # years worth of jokes in. It takes a long time!

    top_joke_ids = reddit.subreddit(SUBREDDIT).top(limit=None)

    for joke_id in top_joke_ids:
        if not db.search(Joke.id == joke_id):
            joke = reddit.submission(id=joke_id)
            db.insert({'id': str(joke.id), 'title': joke.title, 'content': joke.selftext,
                       'score': joke.score, 'subreddit': str(joke.subreddit)})

    # now = one_day_timestamps(datetime(2016,2,3).timestamp())
    now = one_day_timestamps()

    for _ in range(DAYSTOGET):
        now_jokes = reddit.subreddit(SUBREDDIT).submissions(now.start, now.end)
        print('Found jokes on {}.'.format(datetime.fromtimestamp(now.end).date()))
        n = 0
        try:
            for joke in now_jokes:
                if joke.score < 3:
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


def get_joke(joke_type):
    try:
        reddit = connect_to_reddit()
        if joke_type in ['funny', 'hilarious', 'good', 'great', 'something funny', 'something hilarious']:
            joke_type = 'funny'
            joke_list = list(reddit.subreddit('jokes').top(limit=50))

        elif joke_type in ['dirty', 'really dirty', 'something dirty']:
            joke_list = list(reddit.subreddit('dirtyjokes').top(limit=50))
            joke_type = 'dirty'

        elif joke_type in ['dad', 'dad joke']:
            joke_list = list(reddit.subreddit('dadjokes').top(limit=50))
            joke_type = 'dad'

        else:
            joke_list = list(reddit.subreddit('jokes').search(joke_type, limit=30))


        if not joke_list:
            joke_type = "something funny because I couldn't find any jokes about {}.".format(joke_type)
            joke_list = list(reddit.subreddit('jokes').top(limit=40))

        joke_id = random.choice(joke_list)
        joke = reddit.submission(id=joke_id)

        while len(joke.selftext) > 2500:
            joke_id = random.choice(joke_list)
            joke = reddit.submission(id=joke_id)

        joke_title = joke.title.replace(r'\n','').replace('.',' ').replace('nsfw','')
        joke_text = joke.selftext.replace(r'\n','')


        if ' '.join(joke_title.split()[:-1]) in joke_text:
            joke_title = ''

        edits = ['edit:', 'edit1', 'edit 1:', 'edit 1 ']

        for edit in edits:
            if edit in joke_text.lower():
                joke_text = joke_text.lower().split(edit)[0]

        return joke_title, joke_text, joke_type

    except Exception as e:
        return "Whoops, something went wrong. Try again real soon! ".format(e), "Goodbye!", "Oops"


def connect_to_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)

    return reddit

if __name__ == '__main__':
    main()