from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determinerche
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single determiners.

    single_nouns = ["bird", "boy", "car", "cat", "child",
                            "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                            "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns

def test_get_verb():
    # 1. Test the single determiners.

    past_single_verbs = ["drank", "ate", "grew", "laughed", "thought",
                        "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in past_single_verbs

    # 2. Test the plural verbs.

    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(1, "present")


        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in present_single_verbs


    present_multiple_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2, "present")


        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in present_multiple_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2, "future")


        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in future_verbs


def test_get_preposition():
    # 1. Test the single determiners.

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_preposition()

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in prepositions


def test_get_prepositional_phrase():
    # 1. Test the single determiners.

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    single_nouns = ["bird", "boy", "car", "cat", "child",
                            "dog", "girl", "man", "rabbit", "woman"]

    single_determiners = ["a", "one", "the"]


    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        prep_string = str(get_prepositional_phrase(1))
        prep_string = prep_string.split()
        prep_list = list(prep_string)
        # prep_string = prep_string.split

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert len(prep_string) == 3
        assert prep_string[0] in prepositions
        assert prep_string[1] in single_determiners
        assert prep_string[2] in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                            "dogs", "girls", "men", "rabbits", "women"]
    plural_determiners = ["some", "many", "the"]


    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        prep_string = str(get_prepositional_phrase(2))
        prep_string = prep_string.split()
        prep_list = list(prep_string)
        # prep_list = list(prep_list)        # prep_string = prep_string.split


        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert len(prep_string) == 3
        assert prep_string[0] in prepositions
        assert prep_string[1] in plural_determiners
        assert prep_string[2] in plural_nouns

def test_get_adverb():
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

    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_adverb()

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in adverbs 


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
