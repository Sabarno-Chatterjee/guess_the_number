import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS =5

#Function to check user's guess
def check_answer(guess, pick, lives):
    """Checks users guess, returns the number of remaining lives"""
    if guess > pick:
        print("That's a bit high! Take your shot again.")
        return lives - 1
    elif guess < pick:
        print("That's a bit low! Take your shot again.")
        return lives - 1
    else:
        print(f"You won! The answer was {pick}")

#Function to set difficulty
def set_difficulty():
    choice = input("Select a level of difficulty, easy or hard.\n").lower()
    if choice == "easy":
        return EASY_LEVEL_TURNS
    elif choice == "hard":
        return HARD_LEVEL_TURNS

print(art.logo)

def game():
    print("Welcome to the number guessing game.")
    print("I'm thinking of a number between 1 and 100.")
    pick = random.randint(1, 100)
    #Test code:
    #print(f"The correct answer is {pick}")
    lives = set_difficulty()

    guess = 0

    while guess != pick:
        print(f"Current number of lives are {lives}.")
        #Lets the user take a guess
        guess = int(input("Guess a number.\n"))
        lives = check_answer(guess, pick, lives)
        if lives == 0:
            print("Your are out of turns, you lose")
            return
        elif guess != pick:
            print("Guess again")


game()




