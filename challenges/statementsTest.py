#!/usr/local/bin/python3

# Use split() and if to crate a statement that
# prints out words that start with the an s in
# the phrase "Only show words that start with an
# s in this sentence"
myString = 'Only show words that start with an s in this sentence'
for word in myString.split():
    if word.startswith('s'):
        print(word)
print("----------------------\n")


# Use range() to print all even numbers from 0 to 10
for num in range(0, 11):
    if num % 2 == 0:
        print(num)
print("----------------------\n")


# Use List Comprehension to create a list of all numbers
# between 1 and 50 that are evenly divisible by 3
myList = [num for num in range(1, 51) if num % 3 == 0]
# for num in range(1, 51):
#     if x % 3 == 0:
#         myList.append(num)
print(myList)
print("----------------------\n")


# Loop through a string and if the length of the word
# is even print "even"
for word in myString.split():
    if len(word) % 2 == 0:
        print('even')
    else:
        print(word)
print("----------------------\n")


# create a list of numbers from 1 to 100. For multiples
# of 3 print fizz. for multiples of 5 print buzz.
# for numbers that are multiples of both 3 and 5
# print fizzbuzz
myList = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
