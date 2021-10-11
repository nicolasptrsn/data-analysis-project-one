"""
--------------------------------
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import statistics

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
    play_again = input("Would you like to play again? [y/n] ")
    if play_again == 'n':
        print("Thanks for playing. Have a great day!")
    else:
        start_game()
  
    
# TODO Save their attempt number to a list.
# TODO At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
# TODO Ask the player if they want to play again. - The game only replays once, how can I fix this?
    
# Kick off the program by calling the start_game function.
start_game()