# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Calc import Calculos
import math
from Main import ler_Arquivo as read_file
from Main import carregar_Dados


def caso1(data_Hash, coluns, xk, err = 0.01):
    [coef_Corr, coef_Corr_Quad, area_Tail, 
    beta_0, beta_1, yk, rang, upi, lpi] = Calculos(data_Hash, coluns, xk).calcular()

    assert math.isclose(0.954496574, coef_Corr)
    assert math.isclose(0.91106371, coef_Corr_Quad)
    assert math.isclose(0.0000177517, area_Tail, rel_tol=err)
    assert math.isclose(-22.55253275, beta_0)
    assert math.isclose(1.727932426, beta_1)
    assert math.isclose(644.4293838, yk)
    assert math.isclose(230.0017197, rang)
    assert math.isclose(874.4311035, upi)
    assert math.isclose(414.427664, lpi)


def caso2(data_Hash, coluns, xk, err = 0.01):
    [coef_Corr, coef_Corr_Quad, area_Tail, 
    beta_0, beta_1, yk, rang, upi, lpi] = Calculos(data_Hash, coluns, xk).calcular()

    assert math.isclose(0.933306898, coef_Corr)
    assert math.isclose(0,871061766, coef_Corr_Quad)
    assert math.isclose(0.0000798203, area_Tail, rel_tol=err)
    assert math.isclose(-4.038881575, beta_0)
    assert math.isclose(0.16812665, beta_1)
    assert math.isclose(60.85800528, yk)
    assert math.isclose(27.55764748, rang)
    assert math.isclose(88.41565276, upi)
    assert math.isclose(33.3003578, lpi)

def caso3_4(data_Hash, coluns, xk, err = 0.01):
    [coef_Corr, coef_Corr_Quad, area_Tail, 
    beta_0, beta_1, yk, rang, upi, lpi] = Calculos(data_Hash, coluns, xk).calcular()

def main():
    input_Data = "Input.csv"
    data_Hash = carregar_Dados(read_file(input_Data))

    caso1_col = ["Tamanho estimado do proxy", "Tamanho efetivo de adições e modificações"]
    caso2_col = ["Tamanho estimado do proxy", "Tempo efetivo de desenvolvimento (em horas)"]
    caso3_col = ["Tamanho estimado do proxy", "Tamanho efetivo de adições e modificações"]
    caso4_col = ["Tempo efetivo de desenvolvimento (em horas)", "Tamanho efetivo de adições e modificações"]

    caso1(data_Hash, caso1_col, 386)
    caso2(data_Hash, caso2_col, 386)
    caso3_4(data_Hash, caso3_col, 386)
    caso3_4(data_Hash, caso4_col, 386)

main()