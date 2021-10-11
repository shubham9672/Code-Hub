"""
Author : Kanwar Jot Parkash
Date : 8 May 2020
Hangman Game
"""
import random


# picking up the word
def pick_word():
    no = random.randint(1, 267750)
    print("\nLet the game begin.\nHere is your hint:\n")
    with open("words.txt", 'r') as f:
        for m in range(0, no):
            word = f.readline().strip()
    word_length = len(word)
    print("__ " * word_length)
    return word


# guessing the word
def guess_word(word, guess, correct_guesses, all_guesses):
    already_guessed = correct_guesses
    c_word = set(word)
    word_check = "".join(already_guessed)
    correct = False
    g = set(word)
    t = 1
    for s in word_check:
        if s in word:
            t += 1
    if t == len(c_word):
        return 2
    if guess not in already_guessed:
        for i in g:
            if i == guess:
                # correct guess
                already_guessed.add(guess)
                all_guesses.add(guess)
                return 1
    if guess in all_guesses:
        return 3
    if not correct:
        all_guesses.add(guess)
        return 0


print('Welcome to Hangman\nRules of the Game\n\t1. To win this game you have to guess all the letters of the '
      'word.\n\t2. You will be given 6 incorrect guesses')
count = 0
chosen_word = pick_word()
true_guesses = set()
total_guesses = set()
guessed = False
word_list = []
for e in chosen_word:
    # creates a template of the word
    word_list.append("__")
while count < 6 and not guessed:
    letter = input("Please guess a letter from the word: ")
    guessed_letter = letter.upper()
    result = guess_word(chosen_word, guessed_letter, true_guesses, total_guesses)
    if result == 2:
        guessed = True
        print("Congratulations you have guessed the word")
        quit_prgrm = input("Enter q to exit")
    if result == 0:
        count += 1
        guesses_left = 6 - count
        print("You have", guesses_left, "incorrect guesses left")
    elif result == 1:
        place = -1
        for a in chosen_word:
            # placing the correct guesses at their respective palces
            place += 1
            if a == guessed_letter:
                word_list[place] = a
        output_word = " ".join(word_list)
        print(output_word)
    elif result == 3:
        print("You have already guessed that letter")
if count == 6 and not guessed:
    print("The word was: ")
    print(chosen_word)
    quit_prgrm = input("Enter q to exit: ")
