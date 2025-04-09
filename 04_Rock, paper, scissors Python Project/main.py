# Rock, paper, scissors Python Project


import random 

def play_game():
    print("\n🪨 Welcome to Rock, Paper, Scissors!")
    print("Choose one: rock 🪨, paper 📄, or scissors\n")

    choices = ['rock', 'paper', 'scissors']
    user = input("Your choice: ").lower()
    computer = random.choice(choices)

    if user not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"\nYou chose: {user}")
    print(f"💻 Computer chose: {computer}")

    if user == computer :
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")


play_game()
