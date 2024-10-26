import random


print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 100.")
input("Press Enter when you're ready...")

low = 1
high = 100
tries = 0
guessed = False

while not guessed:
    guess = random.randint(low, high)
    print("I guess",guess)
    tries += 1

    feedback = input("Is it too high (H), too low (L), or correct (C)? ").upper()
    if feedback == "C":
        print("I guessed it in",tries,"tries!")
        guessed = True
    elif feedback == "H":
        high = guess - 1
    elif feedback == "L":
        low = guess + 1
    else:
        print("Invalid input. Please enter H, L, or C.")


