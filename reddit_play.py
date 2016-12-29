import random
import praw
from passwords import CLIENT_ID, CLIENT_SECRET, USER_AGENT

def get_joke(joke_type):
    try:
        reddit = connect_to_reddit()
        if joke_type in ['funny', 'hilarious', 'good', 'great']:
            joke_type = 'funny'
            joke_list = list(reddit.subreddit('jokes').top(limit=50))

        elif joke_type == 'dirty':
            joke_list = list(reddit.subreddit('dirtyjokes').top(limit=50))
            joke_type = 'something really dirty'
        else:
            joke_list = list(reddit.subreddit('jokes').search(joke_type, limit=30))


        if not joke_list:
            joke_type = "something funny because I couldn't find any jokes about {}.".format(joke_type)
            joke_list = list(reddit.subreddit('jokes').top(limit=40))

        joke_id = random.choice(joke_list)
        joke = reddit.submission(id=joke_id)

        return joke.title.replace('\n','.'), joke.selftext.replace('\n','.'), joke_type

    except Exception as e:
        return "Whoops, something went wrong. Try again real soon! ".format(e), "Goodbye!"


def connect_to_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)

    return reddit

if __name__ == '__main__':
    joke=get_joke('poop')
    print(joke[0])
    print(joke[1])