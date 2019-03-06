'''
take two inputs: the diameter of a pizza in inches and the cost of that pizza. 
determine the cost per square inch of the pizza. 
The area of a circle is given by Area = pi * radius * radius. 
Note that the size of a pizza is its diameter. 
In other words, a 12-inch pizza has a diameter of 12 inches and a radius of 6 inches.

determine which is the better value: 
a 12-inch pizza costing $14.50 or a 10-inch pizza costing $8.50. 
'''

def calcPizzaCost(diameter, cost):
    radius = diameter * .5
    area = 3.1415 * radius * radius
    return cost / area

twelveInch = calcPizzaCost(12,14.50)
tenInch = calcPizzaCost(10,8.50)

print("Twelve inch pizza cost per sq inch " + str(twelveInch))
print("Ten inch pizza cost per sq inch " + str(tenInch))

if(twelveInch < tenInch):
    print("The twelve inch pizza is a better deal")
else:
    print("The ten inch pizza is better deal")