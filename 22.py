# Initialize an empty list
l1 = []

# Get the number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Input elements for the list
for i in range(n):
    z = int(input("Enter an element for the list: "))
    l1.append(z)

# Print the original list after all elements are added
print("Original list:", l1)

# Define a function to find the second largest number
def sec_largest(lst):
    a = max(lst)    # Find the maximum value
    lst.remove(a)   # Remove the maximum value to find the next largest
    b = max(lst)    # Find the new maximum, which is the second largest
    return b

# Call the function and print the result
c = sec_largest(l1)
print("Second largest number in the list is:", c)
