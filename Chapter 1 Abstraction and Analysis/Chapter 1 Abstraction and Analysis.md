# Chapter 1 Abstraction and Analysis

## Notes

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

