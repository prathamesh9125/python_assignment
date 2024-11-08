# Initialize sets
s1 = set()
s2 = set()
s3 = set()

# Input for the first set
n = int(input("Number of elements for the first set: "))
for i in range(n):
    s1.add(int(input("Enter an element to add to the first set: ")))
print("Set 1 is:", s1)

# Input for the second set
n2 = int(input("Number of elements for the second set: "))
for i in range(n2):
    s2.add(int(input("Enter an element to add to the second set: ")))
print("Set 2 is:", s2)

# Find the intersection of both sets
for i in s1:
    if i in s2:
        s3.add(i)
print("Intersection of both the sets is:", s3)
