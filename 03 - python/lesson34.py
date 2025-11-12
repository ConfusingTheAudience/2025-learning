# MULTITHREADING = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

# 59. 

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f'You finish walking {first}')

def take_out_trash():
    time.sleep(2)
    print('You take out the trash')

def get_mail(adjective, who):
    time.sleep(4)
    print(f'You get the {adjective} mail from {who}')

chore1 = threading.Thread(target=walk_dog, args=('Scooby',))
# we need to use args if our function takes arguments
# args is a tuple
# if we only have one argument we need to end it with ,
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail, args=('important', 'A'))
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print('All chores are complete')

# join method let's us wait till chores are gonna complete to
# take next action