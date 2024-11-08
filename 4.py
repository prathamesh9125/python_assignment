# Take user input for the list
lst = input("Enter the list elements separated by spaces: ").split()
# Convert each element to an integer
lst = [int(x) for x in lst]

# Take user input for the number of positions to rotate
positions = int(input("Enter the number of positions to rotate: "))

# Calculate the effective positions (in case positions > len(lst))
positions = positions % len(lst)

# Rotate the list by slicing
rotated_list = lst[-positions:] + lst[:-positions]

print("Orignal List:",lst)

# Print the rotated list
print("Rotated List:", rotated_list)
