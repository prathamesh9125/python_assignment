n1 = int(input("Enter the number of elements in the first list: "))
list1 = []
for i in range(n1):
    element = int(input("Enter the element: "))
    list1.append(element)
n2 = int(input("Enter the number of elements in the second list: "))
list2 = []
for i in range(n2):
    element = int(input("Enter the element: "))
    list2.append(element)
merged_list = list1 + list2
print("Merged list: ", merged_list)
unique_list = []
for i in merged_list:
    if i not in unique_list:
        unique_list.append(i)
print("List after removing duplicates: ", unique_list)