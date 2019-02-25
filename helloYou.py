#Haley Belcher
#January 24, 2019

def calcAge(x):
    return int(x) * 365

def main():
    name = input("What is your name?")
    age = input('How old are you: ')
    print ("Hello ", name,  " your age is: ", age, 'years old')
    print ("you are", calcAge(age) , " days old")

main()