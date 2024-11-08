# Define the function to find the symmetric difference
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Collect the first set from the user
n1 = int(input("Enter the number of elements in the first set: "))
set1 = set()
for _ in range(n1):
    element = int(input("Enter an element for the first set: "))
    set1.add(element)

# Collect the second set from the user
n2 = int(input("Enter the number of elements in the second set: "))
set2 = set()
for _ in range(n2):
    element = int(input("Enter an element for the second set: "))
    set2.add(element)

# Call the function and print the result
result = symmetric_difference(set1, set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", result)
