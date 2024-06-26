# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:07:06 2024

@author: richc
"""

# https://classroom.google.com/c/NjkwOTE4OTY1MTIx/p/NjgwODcyNjAwMzI2/details

#Purpose: to demonstrate storage of a floating point number
total = 0.0
number1=float(input("Enter the first number: "))
total = total + number1
number2=float(input("Enter the second number: "))
total = total + number2
number3=float(input("Enter the third number: "))
total = total + number3
average = total / 3
print ("The average is " + str(average))
#------------------------------------------------------
#Purpose: to demonstrate storage of a floating point number
number11=float(input("Enter the first number: "))
number12=float(input("Enter the second number: "))
number13=float(input("Enter the third number: "))
total1 = number1 + number2 + number3
average11 = total1 / 3
print ("The average is: ")
print (average11)
#-----------------------------------------------------------
#Purpose: to demonstrate str()
total = 0.0
count = 0
while count < 3:
    number=float(input("Enter a number: "))
    count = count + 1
    total = total + number
average = total / 3
print ("The average is " + str(average))
#-----------------------------------------------------------
# these are string assignments
a = "Hello out there"
print (a)
b = 'Hello'
print (b)
c = "Where's the spam?"
print (c)
d = 'x'
#------------------------------------------------------------
# concatenation of string and integer
a = 'Hello out there'
b = "Where's the spam?"
c = a + b
print (c)
#d = c + 10
# you cannot concatenate a string and an integer
# you must convert the integer to a string first:
d = c + str(10)
print (d)
a = "10"
b = '99'
c = a + b
print (c)
print (type(c))
c = int(c)
print (c)
print (type(c))
#------------------------------------------------------------
# Purpose: Converting one data type to another
number1 = input("Enter first number:\n")
print (number1, type(number1))
number1 = int(number1)
print (number1, type(number1))
#------------------------------------------------------------
# Purpose: Displaying an object's memory location
number1 = input("Enter first number:\n")
print (number1, type(number1), id(number1))
number1 = int(number1)
print (number1, type(number1), id(number1))
#-------------------------------------------------------------
# Purpose: Examples of use of arithmetic operators
print (2 + 4)
print (6 - 4)
print (6 * 3)
print (6 / 3)
print (6 % 3)
print (6 // 3) # floor (integer) division: always truncates fractional remainders
print (-5)
print (3**2) # three to the power of 2
#------------------------------------------------------------------
# Purpose: Examples of use of arithmetic operators with float values
print (2.0 + 4.00)
print (6.0 - 4.0)
print (6.0 * 3.0)
print (6.0 / 3.0)
print (6.0 % 3.0)
print (6.0 // 3.0) # floor (integer) division: always truncates fractional remainders
print (-5.0)
print (3.0**2.0) # three to the power of 2
#-------------------------------------------------------------------
# Purpose: Examples of use of arithmetic operators
# mixing data types in expressions
# mixed type expressions are 'converted up'
# converted up means to take the data type with the greater storage
# float has greater storage (8 bytes) than a regular int (4 bytes)
print (2 + 4.0)
print (6 - 4.0)
print (6 * 3.0)
print (6 / 3.0)
print (6 % 3.0)
print (6 // 3.0) # floor division: always truncates fractional remainders
print (-5.0)
print (3**2.0) # three to the power of 2

#-------------------------------------------------------------------
#PEP 8 Implicit Line Continuation
a = [
    [1,2,3,4,5],
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45],
    ]
type(a)