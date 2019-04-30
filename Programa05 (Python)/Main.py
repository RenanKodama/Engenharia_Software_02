# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Calc_Simpson import Simpson
import collections
import sys


def ler_Arquivo(nomeArquivo):
    arquivo = open(nomeArquivo)
    dadosArquivo = arquivo.readlines()
    arquivo.close()
    return dadosArquivo


def carregar_dados(dadosArquivo):
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
    # file_Name = str(input("Type the name of file: "))
    # hasMap = carregar_dados(ler_Arquivo(file_Name))
    simp = Simpson(0, 5, 0.00001, 9)
    simp.calc()

if __name__ == "__main__":
    main()