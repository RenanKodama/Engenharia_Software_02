# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''


from Calc_Simpson import Simpson
import math

# Debug for func_Sipson()
def test_Simpson():
    result1 = Simpson(0, 1.1, 0.00001, 9, 100).calc()
    result2 = Simpson(0, 1.1812, 0.00001, 10, 100).calc()
    result3 = Simpson(0, 2.750, 0.00001, 30, 100).calc()

    assert math.isclose(0.35006, result1, rel_tol=0.01)
    assert math.isclose(0.36757, result2, rel_tol=0.01)
    assert math.isclose(0.49500, result3, rel_tol=0.01)


def test_Gamma():
    result_int = Simpson(0, 0, 0, 0, 0).func_Gamma(5.0)
    result_float = Simpson(0, 0, 0, 0, 0).func_Gamma(9 / 2)

    assert 24.0 == result_int
    assert math.isclose(result_float, 11.63173, rel_tol=0.01)
