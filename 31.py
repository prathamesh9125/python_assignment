# Define the function to check if a set is a subset of another set
def is_subset(set1, set2):
    return set1.issubset(set2)

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

# Check if set1 is a subset of set2
if is_subset(set1, set2):
    print(f"Set {set1} is a subset of {set2}")
else:
    print(f"Set {set1} is not a subset of {set2}")
