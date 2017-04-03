import random
import praw
from passwords import CLIENT_ID, CLIENT_SECRET, USER_AGENT

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

        joke_title = joke.title.replace(r'\n','').replace('.',' ')
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
    joke=get_joke('king of england')
    print(joke[0])
    print(joke[1])
