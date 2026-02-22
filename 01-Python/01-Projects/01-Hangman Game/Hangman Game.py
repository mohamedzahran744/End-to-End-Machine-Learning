import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: It is the name of a fruit.\n')

    # Print underscores for the word
    for _ in word:
        print('_', end=' ')
    print()

    letter_guessed = ''
    chances = len(word) + 2
    flag = 0  

    try:
        while chances > 0 and flag == 0:
            print()
            chances -= 1

            guess = input('Enter a letter to guess: ').lower()

            # validate input
            if not guess.isalpha():
                print('Enter only LETTERS.')
                continue
            elif len(guess) != 1:
                print('Enter only ONE letter.')
                continue
            elif guess in letter_guessed:
                print('You already guessed that letter.')
                continue

            # add guess if correct
            if guess in word:
                letter_guessed += guess

            # print current progress
            correct = 0
            for char in word:
                if char in letter_guessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')
            print()

            # check win
            if correct == len(word):
                print(f"\nCongratulations! You guessed the word: {word}")
                flag = 1
                break

        # if player lost
        if chances <= 0 and flag == 0:
            print("\nYou lost! Better luck next time.")
            print(f"The word was: {word}")

    except KeyboardInterrupt:
        print("\n\nBye! Try again later.")
        exit()
