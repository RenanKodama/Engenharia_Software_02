# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from ClasseInfo import ClasseInfo


def main():
    arquivo = open('ClasseInfo.py', 'r')
    info = ClasseInfo(arquivo)
    info.countLines()
    info.countClass()
    info.verResultados()
    arquivo.close()


if __name__ == "__main__":
    main()
