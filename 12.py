 #Write a Python program that takes a dictionary of student names as keys and their scores as values. Return the name of the student with th
a = {"Prathamesh": 0, "Pratik": 50, "Ashutosh": 30, "Siddharth": 60, "Mayur": 70}
for i in a:
    if a[i] == max(a.values()):
        print("Name of the student with maximum marks:", i,"with the score", max(a.values()))