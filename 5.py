# Get the number of elements for list1
n = int(input("Enter the number of elements for list 1: "))
list1 = []

# Input elements for list1
for i in range(n):
    element = int(input("Enter element for list 1: "))
    list1.append(element)
print("List 1:", list1)

# Get the number of elements for list2
n2 = int(input("Enter the number of elements for list 2: "))
list2 = []

# Input elements for list2
for i in range(n2):
    element = int(input("Enter element for list 2: "))
    list2.append(element)
print("List 2:", list2)

# Sort list1
list3 = []
while list1:
    m = min(list1)      # Find minimum element
    list3.append(m)     # Add it to the sorted list
    list1.remove(m)     # Remove it from the original list
print("Sorted list 1:", list3)

# Sort list2
list4 = []
while list2:
    m = min(list2)      # Find minimum element
    list4.append(m)     # Add it to the sorted list
    list2.remove(m)     # Remove it from the original list
print("Sorted list 2:", list4)

# Combine the two sorted lists
combined_list = list3 + list4
print("Combined list:", combined_list)
