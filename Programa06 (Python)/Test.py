# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''


from Calc_Simpson_Invertido import Simpson
import math


def test_Caso1():
    p = 0.20
    dof = 6.0
    x = 0.55338
    err = 0.00001

    resultado = Simpson(1.0, dof, p).find_P()

    assert math.isclose(x, resultado, rel_tol = err)


def test_Caso2():
    p = 0.45
    dof = 15
    x = 1.75305
    err = 0.00001

    resultado = Simpson(1.0, dof, p).find_P()

    assert math.isclose(x, resultado, rel_tol = err)


def test_Caso3():
    p = 0.495
    dof = 4
    x = 4.60409
    err = 0.00001

    resultado = Simpson(1.0, dof, p).find_P()

    assert math.isclose(x, resultado, rel_tol = err)
