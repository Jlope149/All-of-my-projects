import random

game = {"r":"Rock", "p":"Paper","s":"Scissors"}
choices = ("r","p","s")


def play_game():
    play = input("Want to Play Rock, Paper, Scissors? (y/n) ").lower()
    if play == "n":
        print("\nThank you for playing!")
    elif play == "y":
        print("\nAlright You Start\n")
    else:
        print("Invalid Input!")
    return play

def get_user_choice():
    while True:
        user_choice = input("Enter Choice: (r/p/s) ")
        if user_choice not in choices:
            print("\nInvalid Input! Try Again")
            continue
        else:
            break
    return user_choice

def get_game_choice():
    game_choice = random.choice(choices)
    return game_choice

def display_choices(user_choice,game_choice):
    print(f"\nYou chose {game[user_choice]}")
    print(f"\nGame chose {game[game_choice]}")


def who_is_the_winner(user_choice, game_choice):
    if user_choice == game_choice:
        print("\nIt's a tie!")
    elif (user_choice == "r" and game_choice == "s") or \
         (user_choice == "s" and game_choice == "p") or \
         (user_choice == "p" and game_choice == "r"):
        print("\nYou win!")
    else:
        print("\nGame wins!")


def main():
    while play_game() == "y":
        user_guess = get_user_choice()
        game_guess = get_game_choice()
        display_choices(user_guess, game_guess)
        who_is_the_winner(user_guess, game_guess)

if __name__ == "__main__":
    main()




