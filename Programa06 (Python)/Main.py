# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Calc_Simpson_Invertido import Simpson

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
    
    for linha in dadosArquivo:
        count_lines += 1

        if count_lines != 1 and len(linha.split(", ")) == 3:
            p = float(linha.split(", ")[0])
            dof = int(linha.split(", ")[1])
            x = float(linha.split(", ")[2])
            
        else:
            print(
                "Erro de formato, era esperado 3 paramentros: PARAM1, PARAM2, PARAM3"
                "Encontrado {} ".format(len(linha.split(", "))) + 
                "na linha {}".format(count_lines)
            )


def main():
    # file_Name = str(input("Name of file: "))
    # carregar_dados(ler_Arquivo(file_Name))
    print(Simpson(1.0, 6, 0.20).find_P())

if __name__ == "__main__":
    main()