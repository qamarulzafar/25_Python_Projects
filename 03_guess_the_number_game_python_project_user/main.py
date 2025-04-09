import random

def guess_number():
    print("\n🎮 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    number = random.randint(1, 100)
    attempts = 0 

    while True:
        try:
            guess = int(input("🔢 Enter Your Guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too Low! Try again.\n")
            elif guess > number:
                print("📈 Too High! Try again.\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts.\n")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")
            

if __name__ == "__main__":
    guess_number()
