 #Using a set, write a Python program that removes duplicate elements from a list and prints the unique elements in the order they appeared i
n = int(input("Enter the number of elements in the list: "))
l1=[]
for i in range(n):
    element = int(input("Enter the element: "))
    l1.append(element)
print("list 1: ", l1)
l3 = set(l1)
print("The elements in order after they appreared in the list are:",list(l3))