 #Write a Python program to compute element-wise sum of given tuples. Original lists: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1) Element-wise sum
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
print("list of tuples",l1)
l4=[]
for i in range(len(l1[0])):
 sum = 0
 for j in range(len(l1)):
     sum+=int(l1[j][i])
 l4.append(sum)
 sum_tuple = tuple(l4)
print("Sum of the said tuples:",sum_tuple)