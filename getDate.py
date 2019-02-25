import datetime

isValidDate = True
inputDate = input("Enter the date in format 'dd/mm/yy' : ")

try:
    day,month,year = inputDate. split('/')
except ValueError:
    isValidDate = False

if isValidDate :
    print("date ok")
else :
    print("You entered the date in the wrong format, please use dd/mm/yy")