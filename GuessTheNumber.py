# This is a Guess the Number game.
import random

guessesTaken = 0
maxNumber = 100

print('Hello! What is your name?')

name = input()

number = random.randint(1, maxNumber)
print('Well, ' + name + ', I am thinking of a number between 1 and ' + str(maxNumber) + '.')

for i in range(6):
    print('Take a guess.')
    guess = input()

    try:
        guess = int(guess)
        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break
    except:
        print('Please type a number between 1 and ' + str(maxNumber))

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
