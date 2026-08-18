# Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format. 
larger_number = int(input("Please enter a number over 100: "))
smaller_number = int(input("Please enter a number under 10: "))
times = larger_number // smaller_number
print("The smaller number goes into the larger number", times, "times.")