"""
EXERCISE 03 - Number guessing game
Topic: while + break + input()

TASK
----
The computer picks a secret number from 1 to 20.
Keep asking the user to guess until they get it right.
After each wrong guess print "Too high" or "Too low".
When they get it right, print how many guesses it took, then break.

Give the user a maximum of 5 attempts. If they run out, reveal the answer.

HINTS
-----
* input() always returns a STRING - convert it with int()
* a while loop needs something that changes, or it runs forever
* Ctrl + C in the terminal stops a runaway program

SAMPLE RUN
----------
Guess a number between 1 and 20: 10
Too low
Guess a number between 1 and 20: 15
Too high
Guess a number between 1 and 20: 13
Correct! You took 3 guesses.
"""

import random

secret = random.randint(1, 20)
attempts = 0
MAX_ATTEMPTS = 5

# TODO: write the while loop here.
#       1. increase attempts
#       2. read a guess with input() and convert it to int
#       3. compare it with secret and print Too high / Too low
#       4. break when correct
#       5. stop after MAX_ATTEMPTS and reveal the secret

while attempts < MAX_ATTEMPTS:
    guess = int(input("Guess a number between 1 to 20 : "))
    attempts += 1

    if guess == secret:
        print(f"Correct Guess \n Number of attempts taken {attempts}")
        break
    elif guess < secret :
        print("Too Low")
    elif guess > secret:
        print("Too High")


else:
    print(f"Max attempts reached! \n The number was {secret}")



        