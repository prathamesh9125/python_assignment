 #Create a Python function that takes a dictionary and returns a new dictionary with all the keys and values swapped.
d3={}
n = int(input("Enter number of key/pair values you want: "))
for i in range(n):
  k = input("Enter your key: ")
  v = input("Enter your value: ")
  d3[k] = v
def swapping_dict(dict):
  swapped_d3={}
  for key, value in d3.items():
    swapped_d3[value] = key
    print(swapped_d3)
swapping_dict(d3)