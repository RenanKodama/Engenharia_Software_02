# -*- coding: utf-8 -*-

''' Universidade Federal do Parana - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import collections
import sys
from Class_StoreCalc import StoreCalc


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


def ver_HashMap(hashMap):
    for key in hashMap.keys():
        print("\tColuna <{}>: \t".format(key)),

        for values in hashMap[key]:
            print(" {}".format(values)),

        print("")


def main():
    dados = ler_Arquivo("ArquivoTeste.csv")
    hash_dados = carregar_dados(dados)
    calculos = StoreCalc(hash_dados, 386)
    calculos.inicializar()


if __name__ == "__main__":
    main()
