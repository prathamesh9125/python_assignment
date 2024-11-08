 #Write a Python program to merge two dictionaries and resolve any key conflicts by summing the values for common keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = dict1.copy()
# Iterate through the second dictionary
for key, value in dict2.items():
  if key in merged_dict:
# If the key exists, sum the values
    merged_dict[key] += value
  else:
    merged_dict[key] = value
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)