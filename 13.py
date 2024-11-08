# Initialize the list and dictionary
final_dict = {}
l1 = []

# Input the number of elements for the list of tuples
n = int(input("Enter the number of tuples: "))

# Input each tuple
for i in range(n):
    a = input("Enter the first element of tuple: ")
    b = input("Enter the second element of tuple: ")
    l1.append((a, b))

# Print the list of tuples
print("List of tuples:", l1)

# Group by the first element of each tuple
for tup in l1:
    key = tup[0]
    value = tup[1]
    if key in final_dict:
        final_dict[key].append(value)
    else:
        final_dict[key] = [value]

# Print the final grouped dictionary
print("Grouped dictionary:", final_dict)
