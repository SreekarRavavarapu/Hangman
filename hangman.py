#Author: Sreekar Ravavarapu
#Email: sravavarapu@umass.edu
#Spire ID: 34515445

import random

def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(phrase, guessed):
    display = ""
    for char in phrase:
        if char.isalpha():
            display += char if char in guessed else "_"
        else:
            display += char
    print(display)

def get_letter(guessed):
    while True:
        letter = input("Please enter a letter: ").upper()
        if not letter.isalpha() or len(letter) != 1:
            print(f'"{letter}" is not a letter!')
        elif letter in guessed:
            print(f'"{letter}" has already been guessed!')
        else:
            return letter

def won(phrase, guessed):
    for char in phrase:
        if char.isalpha() and char not in guessed:
            return False
    return True

def play_game():
    phrase = make_phrase()
    misses = 0
    guessed = []

    print("*** Welcome to Hangman ***")
    print_gallows(misses)

    while not won(phrase, guessed) and misses < 6:
        print_revealed_phrase(phrase, guessed)
        print("Letters guessed:", ', '.join(sorted(guessed)))
        guess = get_letter(guessed)
        guessed.append(guess)

        if guess not in phrase:
            misses += 1
            print_gallows(misses)
        
        if misses == 6:
            print("Game Over!")
            print("Solution was:", phrase)
            break

        if won(phrase, guessed):
            print_revealed_phrase(phrase, guessed)
            print("Congratulations!")

play_game()
