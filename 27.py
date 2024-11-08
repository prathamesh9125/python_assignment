# Define a function to get the lengths of each string in a tuple
def string_lengths(input_tuple):
    lengths = []
    for s in input_tuple:
        lengths.append(len(s))
    return tuple(lengths)

# Input the number of strings
n_strings = int(input("Enter the number of strings you want to input: "))

# Collect strings from the user
input_string = []
for i in range(n_strings):
    string = input(f"Enter string {i + 1}: ")
    input_string.append(string)

# Convert the list of strings to a tuple
input_tuple = tuple(input_string)

# Call the function to get lengths of each string
lengths = string_lengths(input_tuple)

# Print the original and lengths tuples
print("Input Tuple:", input_tuple)
print("Lengths Tuple:", lengths)
