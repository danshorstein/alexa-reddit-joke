from tinydb import Query
import random
import re
from word_stem import stem_search_terms
from common_words import remove_common_words
from open_tiny_joke_db import open_jokes_database

Joke = Query()


def main():
    db = open_jokes_database()
    a = get_joke(db, 'yo mama')
    print(random.choice(a))


def get_joke(db, searchterms):

    if searchterms in ['stuff', 'random', 'funny', 'hilarious',
                       'good', 'great', 'something funny',
                       'something hilarious', 'top', 'very funny']:
        searchterms = 'funny'
        query = db.search(Joke['score'] > 1000)

    elif searchterms in ['dirty', 'really dirty', 'something dirty']:
        query = db.search(Joke['subreddit'] == 'DirtyJokes')
        searchterms = 'dirty'

    elif searchterms in ['dad', 'dad joke']:
        query = db.search(Joke['subreddit'] == 'dadjokes')
        searchterms = 'dad'

    elif searchterms in ['clean']:
        query = db.search(Joke['subreddit'] == 'cleanjokes')
        searchterms = 'clean'

    else:
        split_searchterms = searchterms.split()
        split_searchterms = remove_common_words(split_searchterms)
        split_searchterms = stem_search_terms(split_searchterms)
        query = None
        terms = [re.compile(term) for term in split_searchterms]

        if len(split_searchterms) == 1:
            query = db.search(Joke['content'].search(terms[0]))

        elif len(split_searchterms) == 2:
            query = db.search((Joke['content'].search(terms[0])\
                               & (Joke['content'].search(terms[1]))))

        elif len(split_searchterms) == 3:
            query = db.search((Joke['content'].search(terms[0])
                               & (Joke['content'].search(terms[1]))
                               & (Joke['content'].search(terms[2]))))

        elif len(split_searchterms) == 4:
            query = db.search((Joke['content'].search(terms[0])
                               & (Joke['content'].search(terms[1]))
                               & (Joke['content'].search(terms[2]))
                               & (Joke['content'].search(terms[3]))))

        elif len(split_searchterms) == 5:
            query = db.search((Joke['content'].search(terms[0])
                               & (Joke['content'].search(terms[1]))
                               & (Joke['content'].search(terms[2]))
                               & (Joke['content'].search(terms[3]))
                               & (Joke['content'].search(terms[4]))))

    if len(query) == 0:
        query = db.search(Joke['score'] > 1000)
        searchterms = 'a random topic, because I couldn\'t find any jokes about {}'.format(searchterms)

    joke = random.choice(query)
    title = joke['title']
    content = joke['content']

    title = title.lower().replace('\n','. ').replace('.','. ').replace('nsfw','not safe for work')\
        .replace('tifu','today i fucked up').replace('"',"' ")

    content = content.lower().replace('\n','. ').replace('.','. ').replace('nsfw','not safe for work')\
        .replace('tifu','today i fucked up').replace('"',"' ")

    if ' '.join(title.replace('.','').split()[:-1]) in content:
        title = ''

    edits = ['edit:', 'edit1', 'edit 1:', 'edit 1 ']
    for edit in edits:
        if edit in content.lower():
            content = content.lower().split(edit)[0]

    return title, content, searchterms


if __name__ == '__main__':
    main()
