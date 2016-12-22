# alexa-reddit-joke

I wrote this little Amazon Alexa app using https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development as a guide.

The app lets you search reddit jokes for any search term. It's pretty fantastic. Note that after February, this will not be as easily implemented, 
as Amazon will be stopping the ability to use slot types of AMAZON.LITERAL, which allows you to say anything. 
Instead you will have to supply a list of words that it will accept. See http://tinyurl.com/jo6ygmf for more details. 
So, I suggest you get yours setup before February, so you can be grandfathered in =)

If you want to make your own version, just follow the instructions on the above link to sign up as an Amazon developer and 
download ngrok etc.

This works in Python 3 and Python 2.

You'll need to pip install flask, flask-ask, and praw, get a Reddit API key, and create a passwords.py file containing the reddit keys.

## For the reddit API wrapper you'll need to go on Reddit and sign up for their API.  To do so:

1. Go to https://www.reddit.com/prefs/apps
2. Click "Are you a developer?"
3. Name your app, pick script, the third option, and put any URL you want into the redirect URI box. It's required but doesn't matter what's in there.
4. Grab the list of numbers/letters just below your app name and under "personal use script" - that goes in the client ID in reddit_connect.py.
5. Grab the secret key, which goes in the secret key in reddit_connect.py.

## Amazon App details

* Invocation name, I used "reddit joke" but use whatever you like
* Interaction model - copy and paste from the file "intent_schema"
* For the clean_or_dirty only:  Custom Slot Types - create one that looks like this: Type: CLEAN_OR_DIRTY	 Values: clean | dirty
* Sample utterances - copy and paste from the file. The more you add, the better it will respond to variations.


It should go something like this:
User: "Alexa, ask [invocation name] to tell me a joke about XXXXXXX"
Alexa: "Ok, get ready for a joke about XXXXXXX... {goes on to tell a random joke}"
