

remove_words = ['a', 'the', 'an',
                'or', 'be', 'of',
                'my', 'your', 'his',
                'her', 'its', 'how',
                'why', 'when', 'who',
                'whose', 'which']

def remove_common_words(searchterms):
    #TODO - add more common words to remove

    [searchterms.remove(item) for item in remove_words if item in searchterms]

    return searchterms
