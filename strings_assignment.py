"""
Write a Program to retrieve character 'X' using positive indexing
from "Semantic segmentation of Lung Cancer from Chest X-Ray" string
"""
statement1 = "Semantic segmentation of Lung Cancer from Chest X-Ray"
print(statement1[48])

'''
Write a Program to retrieve the 'L' character from "I have to Love Python Programming" string
using negative/reverse indexing
'''
statement2 = "I have to Love Python Programming"
print(statement2[-23])

'''
Can prove that python string is immutable with the program
'''
statement2[-1] = 'n'
print(statement2)