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
    return question(welcome).reprompt(welcome).simple_card('Jokebox', welcome)


@ask.intent("JokeType")
def tell_joke(joke_type):
    try:
        if joke_type is None:
            joke_type = random.choice(random_topics)
            jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
            msg = "I couldn't understand you, so instead I'll tell you a joke about {}..... ".format(joke_type)

        elif joke_type == 'help':
            help()

        elif joke_type in ('stop', 'cancel'):
            msg = 'Later dude!'
            return statement(msg).simple_card('Jokebox', msg)

        else:
            jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
            msg = 'Ok, get ready for a joke about {}..... '.format(joke_type)

        msg = msg + jokehead + '...' + joke
        return statement(msg).simple_card('Jokebox', msg)
    except Exception as e:
        msg = "Unfortunately I don't feel very funny today. Please try again!"
        return statement(msg).simple_card('Jokebox', msg)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = '''Jokebox is a hilarious app that will tell you a joke about
        whatever you like. For example, you can ask Jokebox for a joke about
        Russia, or you can ask for a pizza party joke.'''
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


if __name__ == '__main__':
    # print(ask_joke_type().__dict__)
    # print(tell_joke('asshole').__dict__)
    app.run(debug=True)
