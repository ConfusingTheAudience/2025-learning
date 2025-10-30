# Shopping cart

foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of a {food}: $'))
        foods.append(food)
        prices.append(price)

print('----- YOUR CART -----')

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f'Your total is: ${total}')




# Two-dimensional keypad

# keypad needs to be in order and if we can pick tuple instead of list we should so we go with tuple

num_pad = ((1, 2, 3), (4, 5 ,6), (7, 8, 9), ('*', 0, '#'))

for row in num_pad:
    for num in row:
        print(num, end=' ')
    print()



# Quiz game

questions = ('Question1', 'Question2', 'Question3', 'Question4', 'Question5')

options = (('A1', 'B1', 'C1', 'D1'), ('A2', 'B2', 'C2', 'D2'), ('A3', 'B3', 'C3', 'D3'), ('A4', 'B4', 'C4', 'D4') , ('A5', 'B5', 'C5', 'D5'))

answers = ('C', 'D', 'A', 'A', 'B')
guesses = [] # we gonna append guesses that's why we use list
score = 0
question_num = 0

for question in questions:
    print('-----')
    print(question)
    for option in options[question_num]:
        print(option, end=" ")
    
    print()
    
    while True:
        picked_answer = input('Enter your answer (A-D): ').upper()
        if picked_answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print('You need to enter A, B, C, or D.')

    guesses.append(picked_answer)

    if picked_answer == answers[question_num]:
        print('Correct!')
        score += 1
    else:
        print(f'Wrong! The correct answer was {answers[question_num]}')

    question_num += 1 

print(f'You have: {score} points')



# Concession stand

menu = {'pizza': 3.00,
        'nachos': 4.50,
        'popcorn': 6.00,
        'fries': 2.50,
        'chips': 1.00,
        'pretzel': 3.50,
        'soda': 3.00,
        'lemonade': 4.25,}

cart = []
total = 0

for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')

while True:
    food = input('Select an item (q to quit): ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=' ')

print()
print(f'Total is: ${total:.2f}')

