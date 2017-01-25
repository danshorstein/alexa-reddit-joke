from nltk import stem

stem_word = stem.snowball.SnowballStemmer("english")


def stem_search_terms(searchterms):
    stemmed_terms = []
    for word in searchterms:
        new_word = stem_word.stem(word)
        if new_word.endswith('i'):
            new_word = new_word[:-1]
        stemmed_terms.append(new_word)

    return stemmed_terms
