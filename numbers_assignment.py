"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
num = 75
PI = 3.14
print(num, type(num), PI, type(PI), sep=' ')

'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
a = 1+2j
b = 3-4J
print(a, type(a), b, type(b), sep=' ')

'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''

digit = 11111111111222222222223333333333344444444444555555555556666666666777777777778888888888899999999999
import sys
print(digit, sys.getsizeof(digit), type(digit), sep='\n')

