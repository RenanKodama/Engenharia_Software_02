# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import collections
from Calc import Calculos

# recycled
def ler_Arquivo(nomeArquivo):
    arquivo = open(nomeArquivo)
    dadosArquivo = arquivo.readlines()
    arquivo.close()
    return dadosArquivo

# recycled
def carregar_Dados(dadosArquivo):
    hashMap = collections.OrderedDict()
    first_line = ""
    count_linhas = 0

    for linha in dadosArquivo:
        count_linhas += 1

        if count_linhas == 1:
            first_line = linha.replace("\n", "")
            for palavras in linha.split(", "):
                hashMap[palavras.replace("\n", "")] = []

        else:
            count_colunas = 0

            for palavras in linha.split(", "):
                hashMap[first_line.split(", ")[count_colunas]].append(
                            palavras.replace("\n", ""))
                count_colunas += 1

    return hashMap


def main():
    # file_name = str(input("Enter the file name: "))
    file_name = "Input.csv"
    data_Hash = carregar_Dados(ler_Arquivo(file_name))
    col = ["Tamanho estimado do proxy", "Tamanho efetivo de adições e modificações"]

    [coef_corr, coef_Quad, area_Tail, 
    beta_0, beta_1, yk, rang, upi, lpi] = Calculos(data_Hash, col, 386).calcular()

    print("Beta0: {}".format(beta_0))
    print("Beta1: {}".format(beta_1))
    print("YK: {}".format(yk))
    print("Range: {}".format(rang))
    print("UPI: {}".format(upi))
    print("LPI: {}".format(lpi))


if __name__ == "__main__":
    main()