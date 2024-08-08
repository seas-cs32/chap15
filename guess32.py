### chap05/guess32.py
import random

def grab_guess():
    # Grab and validate the player's guess
    while True:
        try:
            guess = int(input('Please input your guess: '))
            break
        except ValueError:
            print('Guesses must be an integer. Try again...')
    return guess

def main():
    print('## Welcome to GUESS THE NUMBER! ##')

    secret = random.randint(1, 100)
    # print(f'DEBUG: The secret number is {secret}')

    while True:   # our game loop
        guess = grab_guess()
        # print(f'DEBUG: You guessed {guess}')

        if guess < secret:
            print('Too small!')
        elif guess == secret:
            print('Exactly! You win!')
            break
        else:
            print('Too big!')

if __name__ == '__main__':
    main()