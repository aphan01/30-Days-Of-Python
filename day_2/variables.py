# print('Day 2: 30 Days of python programming')
# Fname = 'An'
# Lname = 'Phan'
# Fullname = Fname + ' ' + Lname
# Country = 'Vietnam'
# City = 'Hanoi'
# Age = 19
# is_married = False
# is_light_on = True
# handsomeness, skills, intelligence = 10, 10, 10


# print(type(Fname))
# print(type(Lname))
# type(Fullname)
# type(Country)
# type(City)
# type(Age)
# print(type(is_married))
# type(is_light_on)
# type(handsomeness)
# print(type(skills))
# type(intelligence)

# print(len(Fname))
# print(len(Lname))
# print(len(Fullname))

# print(len(Fname) > len(Lname))

# num_one = 5
# num_two = 4
# total = num_one + num_two
# diff = num_one - num_two
# product = num_one * num_two
# division = num_one / num_two
# remainder = num_one % num_two
# exponent = num_one ** num_two
# floor_division = num_one // num_two

import math

def maths(rad):
    area_of_circle = 3.14 * rad ** 2
    circum_of_circle = 2 * 3.14 * rad
    return area_of_circle, circum_of_circle

print(maths(10))

fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
full_name = fname + ' ' + lname
country = input('Enter your country: ')
age = int(input('Enter your age: '))

print('This is your information: \nFull Name: {}\nCountry: {}\nAge: {}'.format(full_name, country, age))