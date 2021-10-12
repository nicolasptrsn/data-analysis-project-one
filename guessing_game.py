"""
--------------------------------
Project 1 - Number Guessing Game
--------------------------------
"""

import random
from statistics import mean
from statistics import median
from statistics import mode

scores = []
def start_game():
    # write your code inside this function.
    answer = random.randint(1, 100)
    user_guess = 0
    total_guesses = 0
    
    print("Welcome to **Guess** **That** **Number**")
    print("How to play: Guess a number between 1 and 100!")
    name = input("What's your name? ")
    print("Alrighty then {}, let's go!".format(name))

    while user_guess != answer:
        total_guesses += 1
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < 1 or user_guess > 100:
                raise ValueError
            elif user_guess > answer:
                print("Too high. Try again!")
            elif user_guess < answer:
                print("Too low. Try again!")
        except ValueError:
            print("You must choose a number between 1 and 100. Try again!")
    print("Well done {}! You guessed it in {} tries!".format(name, total_guesses))
    
    scores.append(total_guesses)
    print("**Overall Statistics**")
    print("Mean: {}".format(mean(scores)))
    print("Median: {}".format(median(scores)))
    print("Mode: {}".format(mode(scores)))

    play_again = input("Would you like to play again? [y/n] ")
    if play_again == 'n':
        print("Thanks for playing. Have a great day!")
    else:
        start_game()
      # Kick off the program by calling the start_game function.
start_game()