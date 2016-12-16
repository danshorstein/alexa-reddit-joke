import logging
from flask import Flask
from flask_ask import Ask, statement, question, session
import reddit_connect

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def ask_joke_type():
    welcome = "Oh yay, it's joke time! Do you want it clean or dirty?"
    return question(welcome)

@ask.intent("JokeType")
def tell_joke(joke_type):
    jokehead, joke = reddit_connect.get_joke(joke_type)

    msg = ''

    if joke_type == 'clean':
        msg = "Ok, here's a not quite as dirty joke for you..."
    elif joke_type == 'dirty':
        msg = "Make sure the kids are out of the room, here comes a dirty joke..."

    msg = msg + jokehead + '...' + joke
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
