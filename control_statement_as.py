# Assignment-1: if condition
# Check if a person is eligible to vote based on their age
# Input: Age of the person
# Check if the person is eligible to vote

person_age = int(input("Enter Age: "))
if person_age >= 18:
    print("This Candidate is eligible to vote")

# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative

num = int(input("Enter the number: "))
if num >= 0:
    print('The given number is Positive')
else:
    print('The given number is Negative')

# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd

if num%2 == 0:
    print("And the number is Even")
else:
    print("And the number is Odd")

# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 > num2:
    if num1 > num3:
        print("1st Number is highest")
if num2 > num1:
    if num2 > num3:
        print("2nd Number is highest")
if num3 > num1:
    if num3 > num2:
        print("3rd Number is highest")

# Assignment-5: nested if else condition
"""
Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
amt = 10
age = int(input("Enter the Candidates age: "))
time = int(input("Enter time: "))
zone = input("Enter Zone AM/PM: ")

if zone=='pm' or zone=='PM':
    time +=12

if age<12 or age>65:
    amt *= 0.5

if(time<17):
    amt *= 0.75

print("Estimated Amount: $",amt)

# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population

country_1 = int(input("Enter the population of 1st Country: "))
country_2 = int(input("Enter the population of 2nd Country: "))
country_3 = int(input("Enter the population of 3rd Country: "))

if country_1 > country_2:
    if country_1 > country_3:
        print("Country 1 has biggest population")
    else:
        print("Country 3 has biggest population")
else:
    if country_2 > country_3:
        print("Country 2 has biggest population")
    else:
        print("Country 3 has biggest population")
