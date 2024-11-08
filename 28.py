# Define a function to convert each string in the list to uppercase
def convert_to_uppercase(lst):
    upperlst = []
    for s in lst:
        upperlst.append(s.upper())
    return upperlst

# Input the number of strings
n_strings = int(input("Enter the number of strings you want to input: "))

# Collect strings from the user
input_string = []
for i in range(n_strings):
    string = input("Enter string: ")
    input_string.append(string)

# Call the function to convert strings to uppercase
upper_string = convert_to_uppercase(input_string)

# Print the original and uppercase lists
print("Input List:", input_string)
print("Uppercase List:", upper_string)
