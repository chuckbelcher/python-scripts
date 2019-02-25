'''
Write a Python program that converts miles to kilometers. Specifically, the program should:
1.)Asks the user to enter the number of miles
2.)Convert the number of miles to kilometers and store it in a variable named kilo
3.)Print the message “Your value expressed in kilometers is: “ followed by the value kilo
'''

miles = input("How many miles? ")

def miles_to_kilometers(m):
    return float(m) * 1.609344

kilo = miles_to_kilometers(miles)

print("Your value expressed in kilometers is " + str(kilo))