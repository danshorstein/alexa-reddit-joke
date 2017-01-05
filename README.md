# alexa-reddit-joke

Update: This skill is up on the Amazon skills list as Joke Fairy. https://www.amazon.com/Joke-Fairy-unofficial-Reddit-search/dp/B01N6IMCAP/

I wrote this using https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development as a guide.

The app lets you search reddit jokes for any search term, or you can specify a dirty joke or a dad joke. It's a lot of fun, and people seem to like it!
as Amazon will be stopping the ability to use slot types of AMAZON.LITERAL, but after February you must use a custom slot.
The custom slot still lets you accept any utterances from the users, but the format is just a little different.

If you want to make your own version of this or use it as a guide to make your own skill, just follow the instructions on the above link to sign up as an Amazon developer and
download ngrok etc.

This should work in Python 3 and Python 2.

You'll need to pip install flask, flask-ask, and praw, get a Reddit API key, and create a passwords.py file containing the reddit keys.

## For the reddit API wrapper you'll need to go on Reddit and sign up for their API.  To do so:

1. Go to https://www.reddit.com/prefs/apps
2. Click "Are you a developer?"
3. Name your app, pick script, the third option, and put any URL you want into the redirect URI box. It's required but doesn't matter what's in there.
4. Grab the list of numbers/letters just below your app name and under "personal use script" - that goes in the client ID in passwords.py.
5. Grab the secret key, which goes in the secret key in passwords.py.

## Amazon App details

* Invocation name, I used "reddit joke" but use whatever you like
* Interaction model - copy and paste from the file "intent_schema"
* Sample utterances - copy and paste from the file. The more you add, the better it will respond to variations.

## Hosting

I am hosting this on pythonanywhere.com, on their $5 / month plan for now (but I might try using the free tier or switching to AWS Lambda).
It's super easy to setup, just follow the instructions for the most part.
I created a virtual environment to pip install the required libraries, then you can activate it on pythonanywhere.com.

It should go something like this:
User: "Alexa, ask [invocation name] to tell me a joke about XXXXXXX"
Alexa: "Ok, get ready for a joke about XXXXXXX... {goes on to tell a random joke about XXXXXXX}"
