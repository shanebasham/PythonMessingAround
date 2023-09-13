
NEGATIVE = -1
POSITIVE = 1

def main():
    print("Rosenberg Self-Esteem Scale")
    print("This program is an implementation of the Rosenberg\n\
Self-Esteem Scale. This program will show you ten\n\
statements that you could possibly apply to yourself\n\
Please rate how much you agree with each of the\n\
statements by responding with one of these four letters:\n\
\nD means you strongly disagree with the statement.\n\
d means you disagree with the statement.\n\
a means you agree with the statement.\n\
A means you strongly agree with the statement.\n")

    score = 0
    score += ask_positive_question(
        "1. I feel that I am a person of worth, at least on an"
        " equal plane with others.")
    score += ask_positive_question(
        "2. I feel that I have a number of good qualities.")
    score += ask_negative_question(
        "3. All in all, I am inclined to feel that I am a failure.")
    score += ask_positive_question(
        "4. I am able to do things as well as most other people.")
    score += ask_negative_question(
        "5. I feel I do not have much to be proud of.")
    score += ask_positive_question(
        "6. I take a positive attitude toward myself.")
    score += ask_positive_question(
        "7. On the whole, I am satisfied with myself.")
    score += ask_negative_question(
        "8. I wish I could have more respect for myself.")
    score += ask_negative_question(
        "9. I certainly feel useless at times.")
    score += ask_negative_question(
        "10. At times I think I am no good at all.")

    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

    print("Nature Relatedness Scale Program\n")
    print("This program is an implementation of the Nature\n\
Relatedness Scale developed by Nisbet, Zelenski,\n\
and Murphy. This program will show you 21 statements\n\
that you could possibly apply to yourself. Please\n\
rate how much you agree with each of the statements\n\
by responding with one of these five letters:\n\
\nD means you disagree strongly with the statement.\n\
d means you disagree a little with the statement.\n\
n means you neither agree nor disagree with the statement.\n\
a means you agree a little with the statement.\n\
A means you agree strongly with the statement.\n")

    score = 0
    score += ask_question("1. My connection to nature and the"
        " environment is a part of my spirituality.", POSITIVE)
    score += ask_question("2. My relationship to nature is an"
        " important part of who I am.", POSITIVE)
    score += ask_question("3. I feel very connected to all living"
        " things and the earth.", POSITIVE)
    score += ask_question("4. I am not separate from nature, but a part"
        " of nature.", POSITIVE)
    score += ask_question("5. I always think about how my actions"
        " affect the environment.", POSITIVE)
    score += ask_question("6. I am very aware of environmental issues.",
        POSITIVE)
    score += ask_question("7. I think a lot about the suffering of"
        " animals.", POSITIVE)
    score += ask_question("8. Even in the middle of the city, I notice"
        " nature around me.", POSITIVE)
    score += ask_question("9. My feelings about nature do not affect"
        " how I live my life.", NEGATIVE)
    score += ask_question("10. Humans have the right to use natural"
        " resources any way we want.", NEGATIVE)
    score += ask_question("11. Conservation is unnecessary because"
        " nature is\n    strong enough to recover from any human impact.",
        NEGATIVE)
    score += ask_question("12. Animals, birds and plants have fewer"
        " rights than humans.", NEGATIVE)
    score += ask_question("13. Some species are just meant to die out"
        "or become extinct.", NEGATIVE)
    score += ask_question("14. Nothing I do will change problems in"
        " other places on the planet.", NEGATIVE)
    score += ask_question("15. The state of nonhuman species is an"
        " indicator of the future for humans.", POSITIVE)
    score += ask_question("16. The thought of being deep in the woods,"
        " away\n    from civilization, is frightening.", NEGATIVE)
    score += ask_question("17. My ideal vacation spot would be a"
        " remote, wilderness area.", POSITIVE)
    score += ask_question("18. I enjoy being outdoors, even in"
        " unpleasant weather.", POSITIVE)
    score += ask_question("19. I don’t often go out in nature.",
        NEGATIVE)
    score += ask_question("20. I enjoy digging in the earth and getting"
        " dirt on my hands.", POSITIVE)
    score += ask_question("21. I take notice of wildlife wherever I am.",
        POSITIVE)

    print(f"\nYour score is {score}.")
    print("The lowest possible score is 21.")
    print("The highest possible score is 105.")


def ask_positive_question(statement):
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score

def ask_negative_question(statement):
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score

def ask_question(statement, pos_or_neg):
    print(statement)
    answer = input("  Enter D, d, n, a, or A: ")
    score = 0
    if answer == 'D':
        score = 1
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 4
    elif answer == 'A':
        score = 5
    else:
        score = 3
    if pos_or_neg == NEGATIVE:
        score = 6 - score
    return score

main()