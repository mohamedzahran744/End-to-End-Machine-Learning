# Word Guessing Game – Code Explanation

## Overview
Hangman Wiki:

The origins of Hangman are obscure meaning not discovered, but it seems to have arisen in Victorian times, " says Tony Augarde, author of The Oxford Guide to Word Games. The game is mentioned in Alice Bertha Gomme's "Traditional Games" in 1894 under the name "Birds, Beasts and Fishes." The rules are simple; a player writes down the first and last letters of a word and another player guesses the letters in between. In other sources, [where?] the game is called "Gallows", "The Game of Hangin", or "Hanger". 

Implementation:

This is a simple Hangman game using Python programming language. Beginners can use this as a small project to boost their programming skills and understanding logic.  

The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

---

## How the Code Works

### 1. Importing Required Libraries
```python
import random 
from collections import Counter
```
- `random` → for selecting a random word  
- `Counter` → used to compare guessed letters with the correct word

---

### 2. Creating the List of Words
```python
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')
```
A long string of fruit names is split into a list.

---

### 3. Choosing a Random Word
```python
word = random.choice(someWords)
```
Randomly picks one fruit from the list.

---

### 4. Game Start
```python
print('Guess the word! HINT: word is a name of a fruit')
```
Shows blanks (`_`) for each letter in the word.

---

### 5. Game State Variables
```python
letter_guessed = ''
chance = len(word) + 2
correct = 0
flag = 0
```
- `letter_guessed` → stores letters the player guessed  
- `chance` → number of allowed guesses  
- `flag` → becomes `1` when the player wins  

---

### 6. Main Game Loop
```python
while (chance != 0) and (flag == 0):
```
Runs until:
- The player guesses the whole word  
- OR runs out of chances  

---

### 7. Input Validation
The code checks:
- Only **letters**
- Only **ONE** letter
- Not repeating a guessed letter

---

### 8. Checking Correct Guess
```python
if guess in word:
    k = word.count(guess)
    for _ in range(k):
        letter_guessed += guess
```
If the letter is correct:
- Adds the letter (multiple times if repeated) to `letter_guessed`

---

### 9. Displaying the Progress
```python
for char in word:
    if char in letter_guessed:
        print(char, end=' ')
    else:
        print('_', end=' ')
```

---

### 10. Checking for Win
```python
if Counter(letter_guessed) == Counter(word):
    print("The word is:", word)
    print('Congratulations, You won!')
    flag = 1
    break
```

---

### 11. Losing Condition
If chances run out:
```python
print('You lost! Try again..')
print('The word was {}'.format(word))
```

---

### 12. Keyboard Interrupt Handling
If the user presses **Ctrl+C**:
```python
print('Bye! Try again.')
```

---

## Summary
This script:
- Selects a random fruit name  
- Allows the user to guess letters  
- Manages chances & avoids repeated guesses  
- Shows progress after each guess  
- Declares win/loss  

---

## Notes
Your code contains **indentation errors and typos** (like `if chances <= 0` instead of `chance`).  
If you want, I can **fix the full code** and return a clean version.

---
