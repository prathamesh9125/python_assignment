#Write a python script to find the repeated items of a tuple
n = int(input("Enter number of elements in a tuple: "))
l9=[]
for i in range(n):
  a = input("Enter an element for tuple: ")
  l9.append(a)
  num = set(l9)
print("Input tuple:",tuple(l9))
l10=[]
for i in num:
  count = l9.count(i)
  if count>=2:
    l10.append(i)
print("repeated items:",tuple(l10))