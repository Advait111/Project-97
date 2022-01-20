import random

print('Number Guessing Game')
print('Guess a number (between 1 and 9):')
number=random.randint(1,9)
chances=5

while chances < 6:
    guess=int(input('Enter your guess: '))
    if guess==number:
        print('Congratulations! You won!')
        break
    elif guess<number:
        print('Your guess was too low. Guess a higher number than ', guess)
    else:
        print('Your guess was too high. Guess a lower number than ', guess)
    chances=chances-1
    if chances==0:
        print('You Lose! The number is ', number)
        break