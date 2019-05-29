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
    ''' Leitura de arquivo e estruturação dos dados.

            Parâmetros:
                nomeArquivo:
                    Tipo - String.
                    Descrição - Representa o diretório do arquivo.

            Retorno:
                Retorna valor do tipo dict. Necessário Pandas.
        '''
    return pd.read_csv(nomeArquivo, sep=',')


def main():
    file_name = str(input("Enter the file name:\n \>"))
    col_input = str(input("Select coluns [Ex: coluns_name1, coluna_name2, .., ...]:\n \>"))
    col=[]

    #  Colunas pré configuradas
    # col = [
    #     "Tamanho estimado do proxy",
    #     "Tamanho efetivo de adições e modificações"
    #     ]

    data_Hash = (ler_Arquivo(file_name))

    for colum in col_input.split(", "):
        col.append(colum.strip())

    [
        coef_corr, coef_Quad, area_Tail,
        beta_0, beta_1, yk, rang, upi, lpi,
        total_Time
    ] = Calculos(data_Hash, col, 386).calcular()

    print("\n\n###################### DONE ######################")
    print("\tBeta0: {}".format(beta_0))
    print("\tBeta1: {}".format(beta_1))
    print("\tYK: {}".format(yk))
    print("\tRange: {}".format(rang))
    print("\tUPI: {}".format(upi))
    print("\tLPI: {}".format(lpi))
    print("\tTempo Total: {} min".format(total_Time))


if __name__ == "__main__":
    main()
