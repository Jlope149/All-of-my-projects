import random

running = True
game = ["Rock", "Paper", "Scissor"]
while running:
    play = input("Rock, Paper, Scissors? (y/n) ").lower()
    if play == "n":
        print("\nThank You for Playing!")
        running = False
    elif play == "y":
        print("\nRock \nPaper \nScissors \nShoot")
        user_choice = input("\nEnter choice: (r/p/s) ")
        if user_choice == "r":
            game_choice = random.choice(game)
            print(f"\nGame chose {game_choice}")
            if game_choice == "Rock":
                print("\nYou Tied!\n")
                running = True
            elif game_choice == "Paper":
                print("\nYou Lose!\n")
                running = True
            else:
                print("\nYou Win!\n")
                running = True
        elif user_choice == "p":
            game_choice = random.choice(game)
            print(f"\nGame chose {game_choice}")
            if game_choice == "Rock":
                print("\nYou Win!\n")
                running = True
            elif game_choice == "Paper":
                print("\nYou Tied!\n")
                running = True
            else:
                print("\nYou Lose!\n")
                running = True
        elif user_choice == "s":
            game_choice = random.choice(game)
            print(f"\nGame chose {game_choice}")
            if game_choice == "Rock":
                print("\nYou Lose!\n")
                running = True
            elif game_choice == "Paper":
                print("\nYou Win!\n")
                running = True
            else:
                print("\nYou Tied!\n")
                running = True
        else:
            print("\nInput Invalid! Try Again\n")
            running = True













