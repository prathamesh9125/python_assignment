#Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.
d3={}
n = int(input("Enter number of key/pair values you want: "))
for i in range(n):
 k = input("Enter your key: ")
 v = input("Enter your value: ")
 d3[k] = v
print(d3)
k3 = input("Enter the key you want to replace the existing key with: ")
k2 =  input("Enter the existing key: ")
v2 = input("Enter the value you want to replace: ")
if k2 in d3:
 d3[k3] = v2
 del d3[k2]
else:
 d3[k] = v
print(d3)