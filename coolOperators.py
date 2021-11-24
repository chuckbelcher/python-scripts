#!/usr/local/bin/python3

#import random package
from random import randint, shuffle 

#Create a few arrays of data
ourBikes = ['cb300r', 'cbr300', 'Iron883']
ourYears = [2019, 2019, 2020, 2020, 2021]
myNumbers = [1,2,3,4,5,6,7,8,9,0]

#range operator
for num in range(5):
    #will print the numbers 0,1,2,3,4
    print(num)

for num in range(2,5):
    #same a above but will start at 2 .. 2,3,4
    print(num)

for num in range(2,5,2):
    #same a above but will start at 2 and increment by 2 .. 2,4
    print(num)

#enumerate automaticly iterates.
word = "harley"
for letter in enumerate(word):
    print(letter)

#now lets unpack the tuples
for index, letter in enumerate(word):
    print(index)
    print(letter)

# Zip combines 2+ lists but only for the number 
# of items in the smallest array
for item in zip(ourBikes, ourYears):
    print(item)

#Random shuffle
for i in range(4):
    shuffle(ourBikes)
    print(ourBikes)

#Random Integer between 2 numbers
print(randint(1,10))