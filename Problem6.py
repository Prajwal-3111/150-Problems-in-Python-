# Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format.

slices_start = int(input("How many slices of pizza did you start with? "))
slices_eaten = int(input("How many slices have you eaten? "))
slices_left = slices_start - slices_eaten
print("You have", slices_left, "slices of pizza left.")