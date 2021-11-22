#!/usr/local/bin/python3

#Challenge
# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

#Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check
# and one number to divide by (check). If check divides evenly into num, 
#tell that to the user. If not, print a different appropriate message.

userNumber = int(input('What is your number?: '))
userDivisor = input('What is your divisor, leave blank for odd/even testing: ')

print(userNumber)
if userDivisor:
    print(userDivsor)
else:
    print('Performing odd/even testing ...\n')
    if userNumber % 2 == 0:
        print("Your number %d is even" %(userNumber))
    else:
        print("Your number %d is odd" %(userNumber))


