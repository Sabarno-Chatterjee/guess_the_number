import random
import art

print(art.logo)

numbers = []
for number in range(1, 101):
    numbers.append(number)

pick = random.choice(numbers)

print(pick)

is_match = False
choice = input("Select a level of dificulty, easy or hard.\n").lower()
if choice == "easy":
    lives = 10
elif choice == "hard":
    lives = 5
else:
    print("Invalid entry.\n")
print()
print(f"Current number of lives: {lives}.")
while not is_match:
    guess = int(input("Guess a number between 1 to 100.\n"))
    if guess > pick:
        lives -= 1
        if lives == 0:
            print(f"You lost, the correct number was {pick}.")
            is_match = True
        else:
            print("That's a bit high! Take your shot again.")
            print(f"Remaining number of lives are {lives}.")
            print()
    elif guess < pick:
        lives -= 1
        if lives == 0:
            print(f"You lost, the correct number was {pick}.")
            is_match = True
        else:
            print("That's a bit low! Take your shot again.")
            print(f"Remaining number of lives are {lives}.")
            print()
    elif guess == pick:
        print(f"You won! The answer was {pick}")
        is_match = True