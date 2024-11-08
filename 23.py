# Accept a string input from the user
s = input("Enter a string: ")

# Define the function to count uppercase and lowercase letters
def calc_letters(string):
    count1 = 0  # Lowercase letter count
    count2 = 0  # Uppercase letter count
    for char in string:
        if 122 >= ord(char) >= 97:  # Check if char is lowercase
            count1 += 1
        elif 90 >= ord(char) >= 65:  # Check if char is uppercase
            count2 += 1
    print("No. of Lower case characters:", count1)
    print("No. of Upper case characters:", count2)

# Call the function with the input string
calc_letters(s)
