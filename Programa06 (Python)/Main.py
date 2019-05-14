# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Calc_Simpson_Invertido import Simpson
import math


def ler_Arquivo(nomeArquivo):
    arquivo = open(nomeArquivo)
    dadosArquivo = arquivo.readlines()
    arquivo.close()
    return dadosArquivo


def carregar_dados(dadosArquivo):
    count_lines = 0
    p = 0.0
    dof = 0
    x = 0.0
    eRR = 0.00001

    for linha in dadosArquivo:
        count_lines += 1

        if count_lines != 1:
            if len(linha.split(", ")) == 3:     
                p = float(linha.split(", ")[0])
                dof = int(linha.split(", ")[1])
                x_spected = float(linha.split(", ")[2])
                x_found = Simpson(1.0, dof, p).find_P()
                is_correct(x_spected, x_found, eRR, count_lines)

            else:
                print(
                    "Erro de formato, era esperado 3 paramentros: PARAM1, PARAM2, PARAM3"
                    "Encontrado {} ".format(len(linha.split(", "))) + 
                    "na linha {}".format(count_lines)
                )


def is_correct(val1, val2, eRR, line):
    if(math.isclose(val1, val2, rel_tol= eRR)):
        print("Respostas Conferem na Linha {}".format(line))
    else:
        print(
            "Respostas Não Conferem na Linha {} ". format(line) + 
            "Era esperado {} obteve {}\n\n".format(val1, val2)
        )


def main():
    file_Name = str(input("Name of file: "))
    carregar_dados(ler_Arquivo(file_Name))


if __name__ == "__main__":
    main()
