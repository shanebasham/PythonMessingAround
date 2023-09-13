
import random

def main():
    quantity = 1
    tense = "past"
    print(f'{make_sentence(quantity, tense)}')
    quantity = 1
    tense = "present"
    print(f'{make_sentence(quantity, tense)}')
    quantity = 1
    tense = "future"
    print(f'{make_sentence(quantity, tense)}')

    quantity = 2
    tense = "past"
    print(f'{make_sentence(quantity, tense)}')
    quantity = 2
    tense = "present"
    print(f'{make_sentence(quantity, tense)}')
    quantity = 2
    tense = "future"
    print(f'{make_sentence(quantity, tense)}')

def make_sentence(quantity, tense):
    sentance = f"{get_determiner(quantity).capitalize()} {get_adj()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adv()} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}."
    return sentance

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    if tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    if tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def get_adj():
    adjectives = ["good", "new", "first", "last", "long", "great", "little", "other", "old", "right", "big", "high", 
    "different", "small", "large", "next", "early", "young", "important", "few", "public", "bad", "same"]
    adj = random.choice(adjectives)
    return adj

def get_adv():
    adverbs = ["accidentally", "accusingly", "angrily", "anxiously", "badly", "beautifully", "boldly", "bravely", "breathlessly",
    "carefully", "certainly", "correctly", "dangerously", "eagerly", "effortlessly", "eventually", "finally", "foolishly", "frequently",
    "gladly", "gracefully", "happily", "highly", "hungrily", "ironically", "loudly", "mournfully", "partially", "perfectly",
    "proudly", "quickly", "quietly", "roughly", "sadly", "slowly", "smoothly", "spitefully", "suddenly", "thankfully", "wrongly"]
    adv = random.choice(adverbs)
    return adv

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_adj()} {get_noun(quantity)}"
    return prepositional_phrase 

main()    