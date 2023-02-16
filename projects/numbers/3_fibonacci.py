"""
2_e.py
"""
# Import math Library
import math

def __get_nth_fibonacci_value_from_table__(nth: int) -> float:
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610][nth]

def test(expected_function: callable, test_function: callable, decimal: int)  :
    """ Test """
    expected = expected_function(decimal)
    result = test_function(decimal)

    print(f"n={decimal}\nexpected: {expected}\nresult: {result}")
    return expected == result

def get_nth_fibonacci_value(nth) :
    """
    Enter a number and have the program generate the Fibonacci sequence to that number or
    to the Nth number.
    """
    if nth == 0 :
        return 0

    result = 1
    previous_value = 0
    for _ in range(1, nth) :
        result =  result + previous_value
        previous_value = result - previous_value
    return result

def get_nth_fibonacci_value_recursively(nth) :
    """
    Enter a number and have the program generate the Fibonacci sequence to that number or 
    to the Nth number.
    """
    if nth == 0 :
        return 0
    if nth == 1 :
        return 1
    return get_nth_fibonacci_value_recursively(nth-2) + get_nth_fibonacci_value_recursively(nth-1)


print("Looping function")
for a in range(0, 15) :
    assert test(__get_nth_fibonacci_value_from_table__, get_nth_fibonacci_value, a)
    print(f"Test {a} passed\n")

print("Recursive fonction")
for a in range(0, 15) :
    assert test(__get_nth_fibonacci_value_from_table__, get_nth_fibonacci_value_recursively, a)
    print(f"Test {a} passed\n")
