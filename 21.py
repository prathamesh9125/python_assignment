# Accept a string input from the user
s = input("Enter a string: ")

# Define a function to remove characters with odd index values
def filter_str(s):
    s2 = ""
    for i in range(len(s)):
        if i % 2 == 0:  # Keep characters with even index values
            s2 += s[i]
    return s2

# Call the function and print the filtered string
ab = filter_str(s)
print("Filtered string:", ab)
