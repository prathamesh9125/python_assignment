 #Given a tuple of integers, create a function that converts the tuple into a list and sorts the list.
n = int(input("Enter the number of elements you want in the tuple: "))
l2=[]
for i in range(n):
  a = int(input("Enter an element: in the list: "))
  l2.append(a)
  j = tuple(l2)
print("Orignal tuple:",j)
def convert(tup):
  l3 = list(tup)
  l3.sort()
  print("Sorted list:",l3)
convert(j)