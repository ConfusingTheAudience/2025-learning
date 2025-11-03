# RANDOM NUMBERS

# 22. How to generate random numbers

import random

options = ('rock', 'paper', 'scissors')
cards = ['2', '3', '4', '5', '6', '7']

random.randint(1, 6) # returns random number 1-6
random.random() # returns 0-1 float number
random.choice(options) # returns rock, paper or scissors
random.shuffle(cards) # shuffle things inside