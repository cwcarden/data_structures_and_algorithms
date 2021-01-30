# Chapter 1 Abstraction and Analysis Notes

### Alan Turing 
He conjectured that any problem solvable with a computer only needs the
basic statements that all computer languages have: 
> - Decision statements (if)
> - Looping (for and while)
> - The ability to store and retrieve data.

### Functional Abstraction
> - Decomposes it into a set of functions. Also called procedural abstraction.

### Design by Contract
> **Design by Contract** is using Pre- and Postconditions to specify the modules of a system.
> - **clients** *of the service* - the programs that use the function.
> - **implement** *the serverice* - the code that actually performs the function.
> - **specification** - describes how the function will accomplish the task. The whole point     is that it provides a succint and precise description of a function or component.
        1. Often written in terms of preconditions and postconditions.
        2. Example...

        def sqrt(x):
            """
            Computes the square of x."""

            pre: x is an int or a float and x >= 0
            post: returns the non-negative square root of x
            """
> - **signature** - Information such as:
        1. Name of the function
        2. What parameters required
        3. What if anything the function will return
> - **implementation independence** - The desirable property.
> - **RETVAL** - a name used to indicate the value that was just returned by the function.

### Testing Preconditions
> **Exception Handler** Instead of a program crashing the program transfers control to a special section.

> **Exception objects** In Python run-time errors generate exception objects such as the *ValueError*.
> - **try**, **except**, and **raise** in Python are used for exception handling.

### Top-Down Design
> **Top-Down Design** is the direct application of functional abstraction to decompose a large problem into smaller, more manageable components.

### Algorithm Analysis 
> **Algorithm analysis** allows us to characterize algorithms according to how much time and memory they require to accomplish a task.

### Linear Search
> **Linear search** is searching through the list of items one by one until the target is found. *Moving linearly through memory*.

### Binary Search
> **Binary search** for example looking through a sorted list. The basic idea is that we use two variables to keep track of the endpoints of the range in the list where the item could be.
