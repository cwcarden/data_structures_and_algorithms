"""
Create a list of one million integers numbered 0 to 999,999. Time (using the
time.time function as we did in the examples in this chapter) the worst and
best cases for the list index method version of the linear search, the linear
search code written using a for statement, and the binary search code.  In the
comments list the specifications of your computer (CPU chip and clock speed,
operating system, and Python version) along with the worst and best
times for each of the three searches.
"""
import time


def linear_search_speed(target):
    items = range(1_000_000)
    start = time.time()
    for item in items:
        try:
            my_index = item.index(target)
        except:
            ValueError
    stop = time.time()
    print(f"{target} integer executed in {stop - start} seconds")

linear_search_speed(999999)
linear_search_speed(499999)
linear_search_speed(10)