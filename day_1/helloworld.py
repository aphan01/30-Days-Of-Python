# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+) 
print(3+4)
# subtraction(-)
print(3-4)
# multiplication(*)
print(3*4)
# modulus(%)
print(3%4)
# division(/)
print(3/4)
# exponential(**)
print(3**4)
# floor division operator(//)
print(3//4)




# 3. Write strings on the python interactive shell. The strings are the following:
# Your name
print("John")
# Your family name
print("Doe")
# Your country  
print("USA")
# I am enjoying 30 days of python
print("I am enjoying 30 days of python")





# 4. Check the data types of the following data:
# 10
print(type(10))
# 9.8
print(type(3.14))
# 3.14
print(type(3.14))
# 4 - 4j
print(type(4 - 4j))
# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
# Your name
print(type("John"))
# Your family name
print(type("Doe"))
# Your country
print(type("USA"))


import math

def Eclu_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


x1, x2 = input("Enter x1 and x2 coordinates separated by a comma: ").split(',')
y1, y2 = input("Enter y1 and y2 coordinates separated by a comma: ").split(',')
print("The Euclidean distance between the points is:", Eclu_distance(float(x1), float(y1), float(x2), float(y2)))
