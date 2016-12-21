import logging
from flask import Flask
from flask_ask import Ask, statement, question, session
import reddit_play
import random


app = Flask(__name__)

ask = Ask(app, "/joke_search_for_reddit")

random_topics = ['grandma', 'vegetables', 'dogs',
                 'russia', 'donald trump', 'west africa', 'leftovers']

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
            jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
            msg = "I couldn't understand you, so instead I'll tell you a joke about {}..... ".format(joke_type)

        else:
            jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
            msg = 'Ok, get ready for a joke about {}..... '.format(joke_type)

        msg = msg + jokehead + '...' + joke
        return statement(msg)
    except Exception as e:
        print('Oh no, something went wrong... {}'.format(e))

####EXPERIMENTAL SHIT####
try:
    from cah_randomizer import create_combo

    app2 = Flask('cah_search')

    ask2 = Ask(app2, "/cah_randomizer")

    @ask2.intent("YesIntent")
    def welcome():
        welcome = "Are you ready for some fucked up shit?"
        return question(welcome)

    @ask2.intent("YesIntent")
    def get_cards():

        msg = create_combo()
        return statement(msg)

except:
    print('SOMETHING FUCKED UP')


if __name__ == '__main__':
    # print(ask_joke_type().__dict__)
    # print(tell_joke('asshole').__dict__)
    app.run(debug=True)
    try:
        app2.run(debug=True)
    except:
        pass

