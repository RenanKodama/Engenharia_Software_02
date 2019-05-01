# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Calc_Simpson import Simpson
import sys
import math


def ler_Arquivo(nomeArquivo):
    arquivo = open(nomeArquivo)
    dadosArquivo = arquivo.readlines()
    arquivo.close()
    return dadosArquivo


def carregar_dados(dadosArquivo):
    count_lines = 0
    eRR = 0.00001
    segments = 100

    for line in dadosArquivo:
        count_lines += 1

        if count_lines != 1:
            values = line.split(", ")
            x_init = float(values[0].split(" to x= ")[0])
            x_final = float(values[0].split(" to x= ")[1])
            dof = float(values[1])
            expec_result = float(values[2])
            result = Simpson(x_init, x_final, eRR, dof, segments).calc()
            compare_Results(expec_result, result, count_lines)


def compare_Results(res1, res2, c_line):
    if math.isclose(res1, res2, rel_tol = 0.01):
        print(
            "Respostas Conferem {} e {} na linha {} com 0.01 de tolerância".format(res1, res2, c_line)
            )
    else:
        print("Erro, valores {} e {} não conferem na linha {}".format(res1, res2, c_line))


def main():
    file_Name = str(input("Name of file: "))
    carregar_dados(ler_Arquivo(file_Name))


if __name__ == "__main__":
    main()
