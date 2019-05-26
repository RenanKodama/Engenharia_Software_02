# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Class_StoreCalc import StoreCalc
import collections
import decimal


def test_programa_Caso1():
    caso1 = collections.OrderedDict()
    caso1["Número do Programa"] = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
    caso1["Tamanho estimado do proxy"] = [
        130, 650, 99, 150, 128, 302, 95, 945, 368, 961
        ]
    caso1["Tamanho efetivo das adições e modificações"] = [
        186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601
        ]
    calculos = StoreCalc(caso1, 386)
    resultados = calculos.inicializar()
    
    assert round(decimal.Decimal(-22.55), 2) == round(resultados.beta_0, 2)
    assert round(decimal.Decimal(1.7279), 4) == round(resultados.beta_1, 4)
    assert round(decimal.Decimal(0.9545), 4) == round(resultados.r_xy, 4)
    assert round(decimal.Decimal(0.9111), 4) == round(resultados.r_quadrado, 4)
    assert round(decimal.Decimal(644.429), 3) == round(resultados.yk, 3)


def test_programa_Caso2():
    caso2 = collections.OrderedDict()
    caso2["Número do Programa"] = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
    caso2["Tamanho estimado do proxy"] = [
        130, 650, 99, 150, 128, 302, 95, 945, 368, 961
        ]
    caso2["Tempo efetivo de desenvolvimento"] = [
        15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2
        ]
    calculos = StoreCalc(caso2, 386)
    resultados = calculos.inicializar()

    assert round(decimal.Decimal(-4.039), 3) == round(resultados.beta_0, 3)
    assert round(decimal.Decimal(0.1681), 4) == round(resultados.beta_1, 4)
    assert round(decimal.Decimal(0.9333), 4) == round(resultados.r_xy, 4)
    assert round(decimal.Decimal(0.8711), 4) == round(resultados.r_quadrado, 4)
    assert round(decimal.Decimal(60.858), 3) == round(resultados.yk, 3)


def test_programa_Caso3():
    caso3 = collections.OrderedDict()
    caso3["Número do Programa"] = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
    caso3["Tamanho planejado de adições e modificações"] = [
        163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130
        ]
    caso3["Tamanho efetivo das adições e modificações"] = [
        186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601
        ]
    calculos = StoreCalc(caso3, 386)
    resultados = calculos.inicializar()

    assert round(decimal.Decimal(-23.92), 2) == round(resultados.beta_0, 2)
    assert round(decimal.Decimal(1.43097), 5) == round(resultados.beta_1, 5)
    assert round(decimal.Decimal(0.9631), 4) == round(resultados.r_xy, 4)
    assert round(decimal.Decimal(0.9276), 4) == round(resultados.r_quadrado, 4)
    assert round(decimal.Decimal(528.4294), 4) == round(resultados.yk, 4)


def test_programa_Caso4():
    caso4 = collections.OrderedDict()
    caso4["Número do Programa"] = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
    caso4["Tamanho planejado de adições e modificações"] = [
        163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130
        ]
    caso4["Tempo efetivo de desenvolvimento"] = [
        15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2
        ]
    calculos = StoreCalc(caso4, 386)
    resultados = calculos.inicializar()

    assert round(decimal.Decimal(-4.604), 3) == round(resultados.beta_0, 3)
    assert round(decimal.Decimal(0.140164), 6) == round(resultados.beta_1, 6)
    assert round(decimal.Decimal(0.9480), 4) == round(resultados.r_xy, 4)
    assert round(decimal.Decimal(0.8988), 4) == round(resultados.r_quadrado, 4)
    assert round(decimal.Decimal(49.4994), 4) == round(resultados.yk, 4)
