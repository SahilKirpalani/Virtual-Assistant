import random
import random as r
# ask user for a random number
def randomnumbergame():
    tries = 0
    number = r.randint(1, 20)
    guess = input('I am thinking of a number between 1 and 20. What is it? ')
    tries = tries + 1

    while True:
        if guess.isdigit():
            guess = int(guess)

            if guess > 20 or guess < 1:
                print('Guess between 1-20 ')

            elif guess > number:
                print('Too high')

            elif guess < number:
                print('Too low')

            else:
                print('You got it!')
                break

        else:
            print('Please guess a number.')
        guess = input('Try again: ')
        tries = tries + 1

    if tries == 1:
        print('You have got that after', tries, 'turn')
    else:
        print('That took you', tries, 'goes')


randomnumbergame()