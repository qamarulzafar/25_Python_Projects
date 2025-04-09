# Hangman Python Project


import random 



word_list = ['python', 'hangman', 'challenge', 'programming', 'developer', 'keyboard']


choosen_word = random.choice(word_list)
word_len = len(choosen_word)
lives = 6

guessed_letter = []
display = ['_' for _ in choosen_word]


hangman_stages = [
    '''
     _______
    |/      |
    |      😵
    |      /|\\
    |      / \\
    |
    =========
    ''',
    '''
     _______
    |/      |
    |      😧
    |      /|\\
    |      / 
    |
    =========
    ''',
    '''
     _______
    |/      |
    |      😟
    |      /|\\
    |      
    |
    =========
    ''',
    '''
     _______
    |/      |
    |      😕
    |      /|
    |      
    |
    =========
    ''',
    '''
     _______
    |/      |
    |      😐
    |       |
    |      
    |
    =========
    ''',
    '''
     _______
    |/      |
    |      🙂
    |      
    |      
    |
    =========
    ''',
    '''
     _______
    |/      |
    |      
    |      
    |      
    |
    =========
    '''
]



print("Welcome to Hangman.")


while lives > 0 and '_' in display :
    print(hangman_stages[6 - lives])
    print("Word: ", ' '.join(display))
    print(f"Lives Left: {lives}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letter:
        print("❌ You've already guessed that letter.")
        continue


    guessed_letter.append(guess)

    if guess in choosen_word:
        for i in range(word_len):
            if choosen_word[i] == guess:
                display[i] = guess
        print("Correnct guess!")
    else:
        lives -= 1
        print("Incorrect guess!")
        

if '_' not in display:
    print(hangman_stages[6 - lives])
    print(f"\n🎉 You won! The word was: {choosen_word}")
else:
    print(hangman_stages[6])
    print(f"\n💀 You lost! The word was: {choosen_word}")
