import random

num = random.randint(1, 100)

running = True

while running:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > num:
        print("Too high! Try again.")
        running = True
    elif guess < num:
        print("Too low! Try again.")
        running = True
    else:
        print("Congratulations! You guessed the number!")
        running = False
