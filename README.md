# alexa-reddit-joke

I wrote this little Amazon Alexa app using https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development as a guide.

If you want to use it, you'll have to follow the instructions on the above link to sign up as an Amazon developer and 
download ngrok etc.

You'll also need to pip install flask, flask-ask, and praw. 

## For the reddit API wrapper you'll need to go on Reddit and sign up for their API.  To do so:

1. Go to https://www.reddit.com/prefs/apps
2. Click "Are you a developer?"
3. Name your app, pick script, the third option, and put any URL you want into the redirect URI box. It's required but doesn't matter what's in there.
4. Grab the list of numbers/letters just below your app name and under "personal use script" - that goes in the client ID in reddit_connect.py.
5. Grab the secret key, which goes in the secret key in reddit_connect.py.

## Amazon App details

* Invocation name, I used "reddit joke"
* Interaction model - just copy and paste from the file of that name in this github
* Sample utterances - same, copy and paste from the file in this github. feel free to add more.


It should go something like this:
User: "Alexa, ask reddit joke to tell a dirty joke"
Alexa: "Make sure the kids are out of the room, here comes a dirty joke... {goes on to tell a random joke}"
