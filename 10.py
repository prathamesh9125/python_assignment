 #Create a Python program that takes a set of numbers and returns a new set containing only the even numbers
s1 = set()
s2=set()
n = int(input("number of elements for the set: "))
for i in range(n):
    s1.add(int(input("Enter the element to add in set: ")))
print("Set 1 is:",s1)
for i in s1:
    if i%2==0:
        s2.add(i)
print("Set 2 containing even numbers is:",s2)
