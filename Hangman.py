import random

List_of_words = ["apple", "banana"]


def word_choice():
    word = random.choice(List_of_words)
    split_word = list(word)
    return split_word


def try_count():
    a = len(word_choice()) + 2
    return a


def word_convertor():
    chopped_word = word_choice()
    y = []
    for i in chopped_word:
        y.append("_")
    return y, chopped_word


def letter_checker(i):
    n = 0
    a, b = word_convertor()
    if i in b:
        for d in b:
            if i == d:
                i.replace(d, i)
                print("correct guess!")
    else:
        print("nah you wrong")
        n += 1
    return a, b, i


def main():
    n = 0
    while n < 1:
        m = 0
        tries = try_count()
        underscore, word = word_convertor()

        print("Game: Hangman")
        input("Press Enter to start")
        print("The word has " + str(len(underscore)) + " letters")
        print(underscore)
        while m < 1:
            c = 0
            if c < tries:
                print("You have", tries, "tries")
                guess = input("Guess a letter: ")
                a, b, c = letter_checker(guess)
                print(c)



main()