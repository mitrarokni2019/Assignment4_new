#include <pybind11/pybind11.h>
namespace py = pybind11;


int add(int i, int j) {
    return i + j;
}


int fib(int x) {
    // Your own code here for Assignment 4
    if (x <= 1)
        return x;
    return fib(x - 1) + fib(x - 2);
}


PYBIND11_MODULE(Prog2, m) {
    m.doc() = "pybind11 Prog2 plugin";

    m.def("add", &add, "A function which adds two numbers");
    m.def("fib", &fib, "A function which finds a particular Fibonacci number");
}

