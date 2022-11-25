import art
import random
import replit


def number_guess():
    """Initiates the number guess game"""

    def compare(guess):
        """Takes user guess as the parameter and compares it with the number picked by the computer."""
        if guess > pick:
            return "\nToo high.\n"
        elif guess < pick:
            return "\nToo low.\n"
        else:
            return 0

    print(art.logo)
    print("Welcome to guess the number.\n")
    print("I am thinking of a number between 1-100 and you have to guess it\n")
    pick = random.randrange(1, 101)
    print(f"Test code: {pick}\n")
    level = input("Choose a level 'Easy' or 'Hard'\n").lower()
    lives = 10
    if level == "hard":
        lives = 5

    wrong_guess = True

    while wrong_guess:

        guess = int(input("Take a guess.\n"))
        check = compare(guess)
        if check == 0:
            wrong_guess = False
            print("Bingo, that's the answer.")
        else:
            print(check)
            lives -= 1
            print(f"You have {lives} guesses remaining.\n")
        if lives == 0:
            print("Game over")
            wrong_guess = False


    play = input("Do you want to play Guess the number? 'Yes or No'\n").lower()
    
    if play == "yes":
        replit.clear()
        number_guess()
    else:
        print("Have a nice day!")
    
      
number_guess()

