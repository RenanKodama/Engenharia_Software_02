# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import pandas as pd
import collections
from Calc import Calculos


# recycled
def ler_Arquivo(nomeArquivo):
    return pd.read_csv(nomeArquivo, sep=',')


def main():
    # file_name = str(input("Enter the file name: "))
    file_name = "Input.csv"
    data_Hash = (ler_Arquivo(file_name))
    col = [
        "Tamanho estimado do proxy",
        "Tamanho efetivo de adições e modificações"
        ]

    [
        coef_corr, coef_Quad, area_Tail,
        beta_0, beta_1, yk, rang, upi, lpi,
        total_Time
    ] = Calculos(data_Hash, col, 386).calcular()

    print("Beta0: {}".format(beta_0))
    print("Beta1: {}".format(beta_1))
    print("YK: {}".format(yk))
    print("Range: {}".format(rang))
    print("UPI: {}".format(upi))
    print("LPI: {}".format(lpi))
    print("Tempo Total: {} min".format(total_Time))

if __name__ == "__main__":
    main()
