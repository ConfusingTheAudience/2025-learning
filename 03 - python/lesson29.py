# EXCEPTION = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

# there are many diffrent type of exceptions

# 50. Exception handling

# 1 / 0 - ZeroDivisionError
# 1 + '1' - TypeError
# int('pizza') - ValueError

# try:
#     # some code
# except Exception:
#     # some code
# finally:
#     # some code

try:
    number = int(input('Enter a number: '))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divie by zero")
except ValueError:
    print('Enter only numbers')
except Exception:
    print('Something went wrong')
finally:
    print('Do some cleanup here')


# you can say except Exception but it's not good practice
# since it catches all exceptions instead of specifying the ones you expect
# a good practice is to use it only after handling all specific exceptions

# finally block let us cleanup what we do for example
# when we open the file we want to make sure we close the file at the end
# finally block is executed at the end always