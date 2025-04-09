# Guess the Number (Computer Guesses)


def guess_number():
     print("Think of a number between 1 and 100, and I will try to guess it!")
     input("Press Enter when you're ready...")

     low = 1
     high = 100
     attempts = 0

     while low <= high:
          guess = (low + high) // 2
          attempts += 1
          print(f"My guess is {guess}")
          feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

          if feedback == 'c':
               print(f"I got it in {attempts} attempts!")
               break
          elif feedback == 'h':
               high = guess - 1
          elif feedback == 'l':
               low = guess + 1
          else:
               print("Invalid input. Please enter H, L, or C.")


guess_number()