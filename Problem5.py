# Ask the user to enter three
# numbers. Add together the first
# two numbers and then multiply
# this total by the third. Display the
# answer as The answer is
# [answer]. 

no1 = int(input("Please enter the first number: "))
no2 = int(input("Please enter the second number: "))
no3 = int(input("Please enter the third number: "))
total = (no1 + no2) * no3
print("The answer is",total,".")