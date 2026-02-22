# Number Guessing Game -- Code Explanation

This project is a simple **Number Guessing Game** written in Python.\
The user tries to guess a randomly generated number within a limited
number of attempts.

------------------------------------------------------------------------

##  Overview

The program: 1. Asks the user to enter a lower and upper bound. 2.
Generates a random number within that range. 3. Gives the user **7
chances** to guess the number. 4. Provides hints (too high / too low).
5. Tells the user if they win or lose.

------------------------------------------------------------------------

##  Code Breakdown

### 1️⃣ Importing Required Library

``` python
import random
```

The `random` module helps generate a random number for the guessing
game.

------------------------------------------------------------------------

### 2️⃣ Welcoming the Player

``` python
print("Hi! Welcome to the Number Guessing Game...")
```

Displays a welcome message.

------------------------------------------------------------------------

### 3️⃣ Taking Input for Range

``` python
low = int(input('Enter the Lower Bound: '))
high = int(input('Enter the Upper Bound:'))
```

The user chooses the **range** in which the random number will be
generated.

------------------------------------------------------------------------

### 4️⃣ Generating the Random Number

``` python
num = random.randint(low, high)
```

Creates a hidden random number within the chosen range.

------------------------------------------------------------------------

### 5️⃣ Variables for Counting Attempts

``` python
ch = 7
gc = 0
```

-   `ch` = total allowed chances\
-   `gc` = number of guesses the user has made

------------------------------------------------------------------------

### 6️⃣ The Guessing Loop

``` python
while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))
```

The loop runs until the user uses all 7 guesses.

------------------------------------------------------------------------

### 7️⃣ Checking the Guess

#### ✔️ If the guess is correct:

``` python
if guess == num:
    print(f'Correct! ...')
    break
```

####  If it's the last chance and wrong:

``` python
elif gc >= ch and guess != num:
    print(f'Sorry! The number was {num}...')
```

#### If guess is too high:

``` python
elif guess > num:
    print('Too high!')
```

####  If guess is too low:

``` python
elif guess < num:
    print('Too low!')
```

------------------------------------------------------------------------

##  End Result

The player either wins by guessing the number correctly or loses after
all 7 attempts.

------------------------------------------------------------------------

##  Author

Mohamed Zahran
