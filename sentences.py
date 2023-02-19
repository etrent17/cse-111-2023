import random



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    words = []
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    words = []
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    prep_phrase = ''
    if quantity == 1:
        singular_prep = get_preposition()
        singular_determiner = get_determiner(1)
        singular_noun = get_noun(1)
        prep_phrase = f"{singular_prep} {singular_determiner} {singular_noun}"
    else:
        make_preposition = get_preposition()
        multiple_determiner = get_determiner(2)
        multiple_noun = get_noun(2)
        prep_phrase = f"{make_preposition} {multiple_determiner} {multiple_noun}"
    
    return prep_phrase

def get_adverb():
    adverbs = ['likely',
                'delightfully',
                'yearly',
                'voluntarily',
                'quaintly',
                'originally',
                'queasily',
                'tediously',
                'offensively',
                'curiously',
                'sheepishly',
                'inquisitively'
                ]
    adverb = random.choice(adverbs)
    return adverb


def main():
    words = []
    quantity_val = 0
    v_tense = ''
    quantity = ["single",
                "single",
                "single",
                "plural",
                "plural",
                "plural",
                ]
    verb_tense = ["past",
                "present",
                "future",
                "past",
                "present",
                "future"
                ]
    for i in range(len(quantity)):
        v_tense = verb_tense[i]
        if quantity[i] == "single":
            quantity_val = 1
        elif quantity[i] == "plural":
            quantity_val = 2
        # print(get_determiner(quantity_val))
        # print(get_noun(quantity_val))
        # print(get_verb(quantity_val, v_tense))
        article_val = get_determiner(quantity_val)
        noun_val = get_noun(quantity_val)
        verb_val = get_verb(quantity_val, v_tense)
        prep_string = get_prepositional_phrase(quantity_val)
        adverb_string = get_adverb()
        print(f'{article_val.capitalize()} {noun_val} {adverb_string} {verb_val} {prep_string}.')
if __name__ == "__main__":
    main()