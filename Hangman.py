import random
import nltk
nltk.download('words')
from nltk.corpus import words

WORDS = words.words()

def choose_word():
    return list(random.choice(WORDS))

def get_try_count(word):
    return len(word) + 6

def create_underscore(word):
    return ["_" for _ in word]

def check_letter(guess, word, display):
    if len(guess) != 1:
        print("You can only guess one letter at a time")
        print("You lose a try")
        return True
    elif guess in word:
        for idx, letter in enumerate(word):
            if letter == guess:
                display[idx] = guess
        print("Correct guess!")
        print(display)
        return False
    else:
        print("Wrong guess!")
        print(display)
        print("You lose a try")
        return True

def main():
    print("Game: Hangman")
    word = choose_word()
    tries = get_try_count(word)
    display = create_underscore(word)

    input("Press Enter to start")
    print(f"The word has {len(display)} letters")
    print(display)

    while True:
        if "_" in display:
            if tries > 0:
                guess = input("Guess a letter: ").lower()
                should_decrement = check_letter(guess, word, display)
                if should_decrement:
                    tries -= 1
                print(f"You have {tries} tries left")
            else:
                print("You lose!")
                print(f"The word was: {''.join(word)}")
                break
        else:
            print("You win!")
            print(f"The word was: {''.join(word)}")
            break


main()