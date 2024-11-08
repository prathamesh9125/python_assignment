#Write a Python program to accept n numbers in list and remove duplicates from a list.
n= int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    element = int(input("Enter the element: "))
    list1.append(element)
print("Original list: ", list1)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("List after removing duplicates: ", list2)