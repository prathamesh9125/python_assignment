n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    element = int(input("Enter the element: "))
    list1.append(element)
print("Original list: ", list1)
reverse_list = []
for i in range(len(list1)-1, -1, -1):
    reverse_list.append(list1[i])
print("Reversed list: ", reverse_list)