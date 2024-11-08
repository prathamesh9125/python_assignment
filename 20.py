 #Write a python script to generate Fibonacci terms using generator function.
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
# Creating generator
fib_gen = fibonacci_generator(num_terms)
print("Fibonacci terms:")
for term in fib_gen:
  print(term)