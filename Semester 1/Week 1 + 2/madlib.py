import random

def madlib1():
    print('Please fill in the following:\n')
    food = input('Food item: ')
    plural = ('s')
    if food.endswith(plural):
        it = ('them')
    else:
        it = ('it')
    s_adjective = input('Adjective: ')
    s_animal = input('Animal: ')
    s_verbing = input('Verb ending in -ing: ')
    s_exclamation = input('Exclamation: ')
    s_verb = input('Verb: ')
    s_verb1 = input('Verb: ')
    number = input('Number: ')
    if number == ('1'):
        eggs = ('egg')
    else:
        eggs = ('eggs')
    weight = input('Weight measurment: ')
    adjective = input('Adjective: ')
    verb_ing = input('Verb ending in -ing: ')
    adjective1 = input('Adjective: ')
    adjective2= input('Adjective: ')
    ad_verb = input('Adverb and verb: ')
    noun = input('Noun: ')
    vowel = ('a' , 'e' , 'i' , 'o' , 'u')
    if noun.startswith(vowel):
        noun = ('an ' + (noun))
    else:
        noun = ('a ' + (noun))
    verb = input('Verb: ')
    adj_noun = input('Adjective and noun: ')
    if adj_noun.startswith(vowel):
        adj_noun = ('an ' + (adj_noun))
    else:
        adj_noun = ('a ' + (adj_noun))
    number1 = input('Number: ')
    if number1 == ('1'):
        minute = ('minute')
    else:
        minute = ('minutes')
    body = input('Body part: ')
    exclamation = input('Exclamation: ')

    print('\nYour story is:\n')
    print(f'A {food.upper()} DISASTER!')
    print(f'\nThe other day, I was really in trouble. It all started when I saw a very {s_adjective.lower()} {s_animal.lower()}\n\
    {s_verbing.lower()} down the hallway. "{s_exclamation.upper()}!" I yelled. But all I could think to do was to {s_verb.lower()} over and over.\n\
    Miraculously, that caused it to stop, but not before it tried to {s_verb1.lower()} right in front of my family.\n\
    So I decided to run to the kitchen and make {food.lower()} real fast! I first gathered my ingredients,\n\
    {number} {eggs}, {weight} of milk, flour, sugar, and {adjective.lower()} butter.\n\
    I started {verb_ing.lower()} the {adjective1.lower()} ingredients together in a {adjective2.lower()} bowl,\n\
    then as I tried to {ad_verb.lower()} in the milk, {eggs}, and butter, the {s_animal.lower()} came in! I quickly grabbed {noun.lower()}\n\
    and got ready to {verb.lower()}! After I scooped everything onto {adj_noun.lower()} and\n\
    baked {it} for {number1} {minute}, I grabbed all the {food.lower()} and stuffed {it} in the {s_animal.lower()}s {body.lower()}!\n\
    {exclamation.upper()}!" The {s_animal.lower()} shouted as it tried to {s_verb1.lower()} again in front of me.\n\
    What a disaster!\n')
    return

def madlib2():
    print('Please fill in the following:\n')
    place = input('Place: ')
    noise = input('Noise: ')
    hight = input('Height: ')
    color = input('Color: ')
    adj = input('Adjective: ')
    body = input('Body part: ')
    if body.endswith('s'):
        a = ('')
    verb = input('Verb: ')
    vowel = ('a' , 'e' , 'i' , 'o' , 'u')
    noun = input('Noun: ')
    if noun.startswith(vowel):
        noun = ('an ' + (noun))
    else:
        noun = ('a ' + (noun))
    noun1 = input('Noun: ')
    if noun1.startswith(vowel):
        noun1 = ('an ' + (noun1))
    else:
        noun1 = ('a ' + (noun1))
    body1 = input('Body part: ')
    place1 = input('Place: ')
    adj1 = input('Adjective: ')

    print('\nYour story is:\n')
    print('Camping With a Monster')
    print(f'\nOne night I was camping in {place.capitalize()} when all of a sudden I heard a loud "{noise.upper()}!"\n\
    I turned around and saw a {hight.lower()} monster! It had {color.lower()} hair, {adj.lower()} skin, and {a}\n\
    big, huge, {body.lower()}. It tried to {verb.lower()} me, but I dodged it and hid behind {noun.lower()}.\n\
    I threw {noun1.lower()} at its {body1.lower()} and ran away. When I loked back I saw it was dead!\n\
    So, I went to {place1.lower()} where I knew everything would be {adj1.lower()}.')
    return

def madlib3():
    print('Please fill in the following:\n')
    item = input('Something you take to school: ')
    food = input('Food: ')
    foods = input('Food plural: ')
    utensils = input('Utensils: ')
    drink = input('Drank: ')
    clas = input('Class: ')
    body = input('Bodypart: ')
    place = input('Place: ')

    print(f'\nPacking Your {item.capitalize()}\n')
    print(f'To pack your {item.lower()}, you must first make your lunch. To start, put your {food.lower()}\n\
          in a plastic bag and put it in your lunchbox. Then put a few {foods.lower()} in there with your\n\
          {utensils.lower()}. After that, put in a {drink.lower()} and your lunch is ready!\n\
          Next, stuff the rest of your {clas.lower()} books in the {item.lower()} and then all you\n\
          have to do is put it on your {body.lower()}! Now you are ready to go to {place.lower()}!')
    return

def madlib4():
    print('Please fill in the following:\n')
    clothing = input('Clothing: ')
    space = input('Space object: ')
    aircraft = input('Aircraft: ')
    noun = input('Noun: ')
    spacepl = input('Space object plural: ')
    noun1 = input('Noun: ')
    adjed = input('Adjective ending in -ed: ')
    animal = input('Animal: ')
    name = input('Name: ')
    injury = input('Injury: ')
    shape = input('Shape: ')
    body = input('Body part: ')
    body1 = input('Body part: ')
    color = input('Color: ')
    noun2 = input('Noun: ')
    place = input('Place: ')

    print('\nMystery Flight to Space\n')
    print(f'After I clipped on my space {clothing.lower()} I was ready to go to the {space.lower()}.\n\
        As I was climbing aboard the {aircraft.lower()}, I realized I forgot my {noun.lower()}! So I\n\
        went back and grabbed the {noun.lower()} and then got back on the {aircraft.lower()} and\n\
        blasted away! When we finally made it to outerspace, we lost control of our {noun1.lower()} and\n\
        crashed into giant {spacepl.lower()}. Luckily nobody was {adjed.lower()} except for my pet\n\
        {animal.lower()}, {name.capitalize()}. It had this {shape.lower()} shaped {injury.lower()} on its\n\
        {body.lower()}. When we took a closer look we saw there was something else in there! It had this \n\
        weird {body1.lower()} and a {color.lower()} face. All of a sudden the {noun2.lower()} exploded, \n\
        and nothing else exisited in the entire {place.lower()}.')
    return

def madlib5():
    print('Please fill in the following:\n')
    verb = input('Verb: ')
    mammal = input('Mammal: ')
    verb1 = input('Verb: ')
    letter = input('Letter: ')
    letter1 = input('Letter: ')
    letter2 = input('Letter: ')
    letter3 = input('Letter: ')
    verb2 = input('Verb: ')
    print('\nThe Alphabet\n')
    print(f'To {verb.lower()} the alphabet, you must first ask a {mammal.lower()} how to say it.\n\
        Once they have said it, {verb1.lower()} what they said and it might sound something like this:\n\
        "A, b, c, d, {letter.lower()}, f, g, h, i, {letter1.lower()}, k, l, m, n, o, p, q, r, s, {letter2.lower()},\n\
        u, v, w, {letter3.lower()}, y, and z." Now you can {verb2.lower()} the alphabet!')
    return


# if food.endswith(plural):
    #     it = ('them')
    # else:
    #     it = ('it')
    # s_adjective = input('Adjective: ')
    # s_animal = input('Animal: ')
    # s_verbing = input('Verb ending in -ing: ')
    # s_exclamation = input('Exclamation: ')
    # s_verb = input('Verb: ')
    # s_verb1 = input('Verb: ')
    # number = input('Number: ')
    # if number == ('1'):
    #     eggs = ('egg')
    # else:
    #     eggs = ('eggs')
    # weight = input('Weight measurment: ')
    # verb_ing = input('Verb ending in -ing: ')
    # adjective1 = input('Adjective: ')
    # adjective2= input('Adjective: ')
    # ad_verb = input('Adverb and verb: ')
    # adj_noun = input('Adjective and noun: ')
    # if adj_noun.startswith(vowel):
    #     adj_noun = ('an ' + (adj_noun))
    # else:
    #     adj_noun = ('a ' + (adj_noun))
    # number1 = input('Number: ')
    # if number1 == ('1'):
    #     minute = ('minute')
    # else:
    #     minute = ('minutes')
    # exclamation = input('Exclamation: ')


madlibs = [madlib1, madlib2, madlib3]
randmadlib = random.choice(madlibs)
print(randmadlib())