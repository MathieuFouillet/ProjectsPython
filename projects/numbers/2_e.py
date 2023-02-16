"""
2_e.py
"""
# Import math Library
import math

def __get_nth_decimal_of_e_from_math_module__(decimal: int) -> float:
    return round(math.e, decimal)

def test(expected_function: callable, test_function: callable, decimal: int)  :
    """ Test """
    expected = expected_function(decimal)
    result = test_function(decimal)

    print(f"n={decimal}\nexpected: {expected}\nresult: {result}")
    return expected == result

def get_nth_decimal_of_e(decimal) :
    """
    Find PI to the Nth Digit using BPP formula
    https://fr.wikipedia.org/wiki/Formule_BBP#Et_pour_le_calcul_des_d%C3%A9cimales_?
    """
    result = 0
    for k in range(0, decimal + 5) :
        result +=  1/math.factorial(k)
    print(result)
    return round(result, decimal)


for a in range(0, 100) :
    assert test(__get_nth_decimal_of_e_from_math_module__, get_nth_decimal_of_e, a)
    print(f"Test {a} passed\n")
