# Number guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f'Select a number between {lowest_num} and {highest_num}')

while is_running:
    guess = input('Enter your guess: ')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print('That number is out of range')
            print(f'Select a number between {lowest_num} and {highest_num}')
        elif guess < answer:
            print('Too low! Try again')
        elif guess > answer:
            print('Too high! Try again')
        else:
            print(f'Correct. The answer was {answer}')
            print(f'Number of guesses: {guesses}')
            is_running = False
    else:
        print('Invalid guess')
        print(f'Select a number between {lowest_num} and {highest_num}')



# Rock, paper, scissors game

options = ('rock', 'paper', 'scissors')
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (rock, paper, scissors): ')

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        print("It's a tie")
    elif player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    else:
        print('You lose!')

    if not input('Play again? (y/n): ').lower() == 'y':
        running = False

print('Thanks for playing!')