
from Prog2 import fib as fib_c
from time import perf_counter as pc
from time import sleep as pause
import matplotlib.pyplot as plt




def fib_py(n):
    if n in (0,1) :
        return n 
    else: 
        return fib_py(n-1)+fib_py(n-2)


if __name__ == "__main__":
    
    for i in range(35,45):
         start = pc()
         fib_c(i)
         
         end = pc()
         print(f"Process took {round(end-start, 2)} seconds in C++ for i  {i}")



print(fib_py(5))

if __name__ == "__main__":
    for i in range(35,45):
        start = pc()
        fib_py(i)
        end = pc()
        print(f"Process took {round(end-start, 2)} seconds in python for i  {i}")






plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()