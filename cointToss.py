import random

guess = ''
toss = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

result = random.randint(0, 1)

if result == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    
    guess = input()
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
