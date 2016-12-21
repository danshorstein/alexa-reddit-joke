import praw

def get_joke(joke_type):
    try:
        if joke_type != 'dirty':
            joke_type == 'clean'
        reddit = connect_to_reddit()
        joke_id = reddit.subreddit({'clean':'Jokes','dirty':'DirtyJokes'}[joke_type]).random()
        joke = reddit.submission(id=joke_id)
        return joke.title.replace('\n','.'), joke.selftext.replace('\\','.')

    except Exception as e:
        return "I don't know what {} means. Please say clean or dirty next time.".format(e), "Goodbye!"

def connect_to_reddit():
    reddit = praw.Reddit(client_id='pFbU5k49nrTu6g',
                         client_secret='uWHqHonDqZkdi9emqs-I4gI2RD0',
                         user_agent='amazon-alexa:Alexa Jokes:v0.0.1 (by /u/dtizzlenizzle)',
                         username='dtizzlenizzle',
                         password='Snoope33')
    print(reddit.user.me())
    return reddit


if __name__ == '__main__':
    print(get_joke('dirty'))
