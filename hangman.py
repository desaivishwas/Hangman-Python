# Author - Vishwas Desai
# Hangman game
import random


def announcement():
    print("H A N G M A N")


def hint(word):
    a = word[0:3]
    b = ("-" * (len(word) - 3))
    return a + b


def generate_word():
    words = ['python', 'java', 'kotlin', 'javascript']
    gen_word = random.choice(words)
    return gen_word


def guess_word(word, actual):
    if word == actual:
        print("You guessed the word!\nYou survived!")
    else:
        print("You lost!")


def game():
    init = "-" * len(ans)
    keys = list(ans)
    values = list(init)
    # wrong counter
    guesses = 0
    guess_list = []
    while guesses < 8:
        print()
        print(init)
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
        else:
            if ord(letter) not in range(97, 123):
                print("Please enter a lowercase English letter")
            else:
                if letter in guess_list:
                    print("You've already guessed this letter")
                else:
                    if letter in keys:
                        idx = [i for i, e in enumerate(keys) if e == letter]
                        if len(idx) > 1:
                            for index in idx:
                                values[index] = letter
                        else:
                            values[idx[0]] = letter
                        res = ''.join(i for i in values)
                        init = res
                        if init == ans:
                            break
                    else:
                        print("That letter doesn't appear in the word")
                        guesses += 1
                    guess_list.append(letter)
    guess_word(init, ans)


if __name__ == '__main__':
    announcement()
    ans = generate_word()
    while True:
        play = input('Type "play" to play the game, "exit" to quit:')
        if play == "play":
            game()
        else:
            break
