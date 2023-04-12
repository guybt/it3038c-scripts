import random

randomNumber = random.randint(1,10)
guess = int(input('Guess a number 1-10'))

if guess == randomNumber:
    print('You got it right!')
elif guess < randomNumber:
    print('Too low')
else:
    print('Too high')

print('The random number was ', randomNumber)