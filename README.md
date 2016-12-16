# alexa-reddit-joke

I wrote this little Amazon Alexa app using https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development as a guide.

There are two versions. 

clean_or_dirty - The first one you can only search for "Clean" or "Dirty" jokes. However please note
that most of the "clean" jokes are actually dirty anyways. These come from /r/Jokes, which has jokes of all levels of appropriateness.

joke_search - This newer and more awesome search lets you search for ANY one or two word search term. It's pretty fantastic. However, please note that after February, this will not be as easily implemented, as Amazon will be stopping the ability to use slot types of AMAZON.LITERAL, which allows you to say anything. Instead you will have to supply a list of words that it will accept. See http://tinyurl.com/jo6ygmf for more details. So, I suggest you get yours setup before February, so you can be grandfathered in =)

This is not difficult to add to your own Alexa! Just follow the instructions on the above link to sign up as an Amazon developer and 
download ngrok etc.

This was designed in Python 3, and I have no idea if it works in Python 2.

You'll need to pip install flask, flask-ask, and praw. 

## For the reddit API wrapper you'll need to go on Reddit and sign up for their API.  To do so:

1. Go to https://www.reddit.com/prefs/apps
2. Click "Are you a developer?"
3. Name your app, pick script, the third option, and put any URL you want into the redirect URI box. It's required but doesn't matter what's in there.
4. Grab the list of numbers/letters just below your app name and under "personal use script" - that goes in the client ID in reddit_connect.py.
5. Grab the secret key, which goes in the secret key in reddit_connect.py.

## Amazon App details

* Invocation name, I used "reddit joke"
* Interaction model - just copy and paste from the file of that name in this github
* Custom Slot Types - create one that looks like this: 
  Type: CLEAN_OR_DIRTY	
  Values: clean | dirty
* Sample utterances - same, copy and paste from the file in this github. feel free to add more.


It should go something like this:
User: "Alexa, ask reddit joke to tell a dirty joke"
Alexa: "Make sure the kids are out of the room, here comes a dirty joke... {goes on to tell a random joke}"
