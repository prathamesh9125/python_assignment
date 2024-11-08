 #Write a Python program to convert a tuple of string values to a tuple of integer values. Original tuple values: (('333', '33'), ('1416', '5
n = int(input("Enter the number of tuples you want in 1 tuple: "))
l1=[]
for i in range(n):
 l2 = []
 a = input("Enter element 1 of tuple: ")
 b = input("Enter element 2 of tuple: ")
 l2.append(a)
 l2.append(b)
 c = tuple(l2)
 l1.append(c)
print("Original tuple",tuple(l1))
l3 =[]
for tup in l1:
 con_tup = tuple(int(num) for num in tup)
 l3.append(con_tup)
print("Updated tuples are:",tuple(l3))