#!/usr/local/bin/python3

#Challenge
# Create a program that asks the user to enter their name 
# and their age. Print out a message addressed to them 
# that tells them the year that they will turn 100 years old.

# Extras
# Add on to the previous program by asking the user 
# for another number and printing out that many copies 
# of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message 
# on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

UserName = input("Enter your Name: ")
UserAge = int(input("Enter your age: "))
YearsTil100 = (100 - UserAge)
NumberStatements = int(input("How many times would you like to print the message: "))

for x in range(NumberStatements):
    print("Hello %s you will be 100 in %d years\n" %(UserName, YearsTil100))