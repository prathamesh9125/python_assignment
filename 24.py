 #Create a function that counts the frequency of each word in a given sentence using a dictionary.
s = input("Enter a string: ")
def calc_freq(string):
  b={}
  a = set(string)
  for i in string:
    count = string.count(i)
    b[i] = count
  print(b)
calc_freq(s)