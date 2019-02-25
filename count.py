#Write a program that loops through 0-99 and sums them up

sum = 0
counter = 0

'''
while counter < 100:
    sum += counter
    counter += 1
    print(sum)
'''

for i in range(0,99):
    sum += i
    print(sum)
