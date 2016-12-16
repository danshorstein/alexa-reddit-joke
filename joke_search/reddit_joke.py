import logging
from flask import Flask
from flask_ask import Ask, statement, question, session
import reddit_connect
import random

app = Flask(__name__)

ask = Ask(app, "/")

random_topics = ['balls', 'dead people', 'grandma', 'midget porn', 'masturbation',
                 'russia', 'donald trump', 'west africa', 'leftovers', 'virgins']

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def ask_joke_type():
    welcome = "Welcome! What kind of joke would you like to hear?"
    return question(welcome)

@ask.intent("JokeType")
def tell_joke(joke_type):
    try:
        if joke_type is None:
            joke_type = random.choice(random_topics)
            msg = "I couldn't understand you, so instead I'll tell you a joke about {}..... ".format(joke_type)

        else:
            msg = 'Ok, get ready for a joke about {}..... '.format(joke_type)

        jokehead, joke = reddit_connect.get_joke(joke_type)
        msg = msg + jokehead + '...' + joke
        return statement(msg)
    except Exception as e:
        print('Shit. {}'.format(e))
if __name__ == '__main__':
    # print(ask_joke_type().__dict__)
    # print(tell_joke('asshole').__dict__)
    app.run(debug=True)
