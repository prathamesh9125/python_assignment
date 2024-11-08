 #Write a python program to count repeated characters in a string.
 #Sample string: 'the quick brown fox jumps over the lazy dog'. Expected output: o-4, e-3, u-2, h-2, r-2, t-2, ‘ ’-7.
s = input("Enter the string: ")
l=set()
for char in s:
 l.add(char)
for i in l:
 count = s.count(i)
 if count>=2:
    print(i,"-",count,"times")