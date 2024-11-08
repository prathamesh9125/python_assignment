#Write a Python script to generate and print a dictionary which contains a number (between 1 and n) in the form(x, x*x). Sample Dictionary (
d4={}
n = int(input("Enter number of elements for dictionary: "))
for i in range(1,n+1):
     d4[i] = i*i
print(d4)