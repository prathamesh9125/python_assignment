# Input the number of elements for the tuple
n = int(input("Enter the number of elements you want in the tuple: "))
l2 = []

# Collect elements for the tuple
for i in range(n):
    a = int(input("Enter an element in the tuple: "))
    l2.append(a)

# Convert the list to a tuple
j = tuple(l2)
print("Original tuple:", j)

# Define a function to calculate the sum of elements in a tuple
def sum_calc(lst):
    total = 0
    for i in lst:
        total += i
    return total

# Call the function and print the result
result = sum_calc(j)
print("Sum of elements in the tuple:", result)
