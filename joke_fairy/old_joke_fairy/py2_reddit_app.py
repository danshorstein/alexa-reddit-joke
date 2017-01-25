import logging
import random
from flask import Flask
from flask_ask import Ask, statement, question, session

import joke_fairy.old_joke_fairy.reddit_play as reddit_play

app = Flask(__name__)

ask = Ask(app, "/joke_search_for_reddit")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def ask_joke_type():
    welcome = "Welcome! What kind of joke would you like to hear?"
    return question(welcome).reprompt('What kind of joke would you like?')


@ask.intent("JokeType")
def tell_joke(joke_type=None):
    try:
        if joke_type is None:
            joke_type = 'funny'
            jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
            msg = "I couldn't understand you, so instead I'll tell you one of my favorite jokes. "


        else:
            jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
            if joke_type in ['funny', 'dirty', 'dad']:
                msg = 'Oh boy, here comes one of my favorite {} jokes.... '.format(joke_type)

            else:
                msg1 = 'Ok, get ready for a joke about {}..... '.format(joke_type)
                msg2 = 'All right, here is one of my favorite jokes about {}..... '.format(joke_type)
                msg3 = 'Ready or not, here comes a joke about {}..... '.format(joke_type)

                msg = random.choice([msg1, msg2, msg3])

        msg = msg + jokehead + '...' + joke
        msg2 = msg.lower().replace('shit', 'sh-it')\
            .replace('fuck', 'fu-ck')\
            .replace('asshole', 'ass hole')\
            .replace('..', '.. ')\
            .replace('http://','')\
            .replace('https://','')\
            .replace('goddamn', 'god damn')\
            .replace('bitch', 'bit-ch')
        return statement(msg2).simple_card('Joke Fairy', msg)

    except Exception as e:
        joke_type = 'funny'
        jokehead, joke, joke_type = reddit_play.get_joke(joke_type)
        msg = "I couldn't understand you, so instead I'll tell you a random funny joke. "
        msg = msg + jokehead + '...' + joke
        return statement(msg).simple_card('Joke Fairy', msg)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'Joke fairy is an unofficial Reddit joke search app that ' +\
      'will tell you a joke about whatever you like. ' +\
      'For example, you can ask Joke fairy for a joke about Russia, ' +\
      'or you can ask for a dirty joke, a funny joke, or a dad joke. What kind of joke would ' +\
      'you like to hear?'
    reprompt_text = 'What kind of joke would you like?'
    return question(speech_text).reprompt(reprompt_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    msg = 'Smell you later!'
    return statement(msg)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    msg = 'Smell you later!'
    return statement(msg)


if __name__ == '__main__':
    # print(ask_joke_type().__dict__)
    print(tell_joke('dirty').__dict__)
    # app.run(debug=True)
