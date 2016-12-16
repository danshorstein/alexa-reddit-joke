import random
import praw

CLIENT_ID = ''
CLIENT_SECRET = ''
USERNAME = ''
PASSWORD = ''

def get_joke(joke_type):
    try:
        reddit = connect_to_reddit()
        joke_list = list(reddit.subreddit('Jokes').search(joke_type, limit=100))
        joke_id = random.choice(joke_list)
        joke = reddit.submission(id=joke_id)

        print('We found a total of {} jokes about {}.'.format(len(joke_list), joke_type))

        return joke.title.replace('\n','.'), joke.selftext.replace('\\','.')

    except Exception as e:
        return "Oh shit, something went wrong. {}. ".format(e), "Goodbye!"

def connect_to_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent='amazon-alexa:Alexa Jokes:v0.0.1 (by /u/{})'.format(USERNAME),
                         username=USERNAME,
                         password=PASSWORD)

    return reddit


if __name__ == '__main__':
    joke=get_joke('poop')
    print()
    print(joke[0])
    print()
    print(joke[1])
    print()
