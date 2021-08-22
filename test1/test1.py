
# Program for displaying fibonacci series using recursion
n = int(input("Enter The number of terms : "))
first = 0
second = 1
# Function for calculating fibonacci number
def fib(n):
    if n <= 1:
        return n
    # performing recursion
    return fib(n - 1) + fib(n - 2)
# displaying the fibonacci series for n terms
for i in range(0, n+1):
    print(fib(i))