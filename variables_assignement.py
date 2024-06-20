"""
Assignment-1:
WAP to assign 3 values (string, int, float)
to 3 variables (Student_name, Roll_Number, Percentage_of_marks).
print the values using print function.
"""

Student_name = "Sakshi Pimparwar"
Roll_Number = 64
Percentage_of_marks = 79.85

print("name: " ,Student_name,"Roll No: " ,Roll_Number,"Percentage: ",Percentage_of_marks, sep="\n")

"""
Assignment-2:
WAP to assign value 6 to two different variables (example: a1, b1) 
using single line of code.
Check the variable values and memory address.
"""

a = b = 6
print(a,b,sep=" ")
print(id(a),id(b))

"""
Assignment-3:
WAP to assign multiple values to multiple variables
in single line of code
After assigning, print and check the values
"""

l,i,f,e = 12,9,6,5
print(l,i,f,e)