import random

running = True

while running:
    roll = input("Would you like to roll the dice? (y/n) ")
    if roll == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"You rolled a {die1} and a {die2}.")
        if die1 == die2:
            print("You rolled a double!")
    elif roll == "n":
        print("Thanks for Playing!")
        running = False
    else:
        print("Invalid input. Please try again.")
        running = True


