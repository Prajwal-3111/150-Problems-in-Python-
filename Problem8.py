# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

total_bill = float(input("Please enter the total price of the bill: "))
num_diners = int(input("Please enter the number of diners: "))
amount_per_person = total_bill / num_diners
print("Each person must pay:", amount_per_person) 