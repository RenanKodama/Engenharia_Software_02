# -*- coding: utf-8 -*-

''' Universidade Federal do Parana - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import decimal
import math
import collections
import sys


class Calc:
    def __init__(self, hasMap):
        self.hasMap = hasMap
        self.total_LogaritmoXY = decimal.Decimal(0)
        self.total_LogaritmoXY_AVG = decimal.Decimal(0)
        self.avg = decimal.Decimal(0)
        self.variancia = decimal.Decimal(0)
        self.desvioPadrao = decimal.Decimal(0)
        self.faixasLOG = collections.OrderedDict()
        self.faixasNORM = collections.OrderedDict()

    def inicializar(self):
        self.divisao_XY()
        self.logaritmo_X_por_Y_Media()
        self.calcular_Variancia()
        self.calcular_DesvioPadrao()
        self.calcular_Faixas_Log()
        self.calcular_Faixas_Normal()
        self.ver_resultados()
        return(self.faixasNORM)

    def divisao_XY(self):
        if len(self.hasMap.keys()) == 2:
            self.hasMap["Dx"] = []
            key_short = list(self.hasMap.keys())[1]
            for valores in self.hasMap[key_short]:
                self.hasMap["Dx"].append(decimal.Decimal(valores))

        elif len(self.hasMap.keys()) == 3:
            self.hasMap["Dx"] = []
            key1 = list(self.hasMap.keys())[1]
            key2 = list(self.hasMap.keys())[2]
            v1_aux = []
            v2_aux = []

            for valores in self.hasMap[key1]:
                v1_aux.append(decimal.Decimal(valores))

            for valores in self.hasMap[key2]:
                v2_aux.append(decimal.Decimal(valores))

            for i in range(len(v1_aux)):
                self.hasMap["Dx"].append(decimal.Decimal(v1_aux[i] / v2_aux[i]))

        else:
            self.hasMap["Dx"] = []
            print("Muitas Colunas! Selecione uma para os Cálculos")
            key_input = str(input("Nome da coluna: ")).strip()

            if self.hasMap.__contains__(key_input):
                for valores in self.hasMap[key_input]:
                    self.hasMap["Dx"].append(decimal.Decimal(valores))
            else:
                print("Coluna não Encontrada!")

    def logaritmo_X_por_Y_Media(self):
        self.hasMap["lg(Dxy)"] = []
        v1Log_aux = []

        for valores in self.hasMap["Dx"]:
            v1Log_aux.append(valores)

        for i in range(len(v1Log_aux)):
            valor = v1Log_aux[i]
            self.hasMap["lg(Dxy)"].append(decimal.Decimal(math.log(valor, math.e)))

        for valores in self.hasMap["lg(Dxy)"]:
            self.total_LogaritmoXY += valores

        self.avg = decimal.Decimal(self.total_LogaritmoXY / len(self.hasMap["lg(Dxy)"]))

    def calcular_Variancia(self):
        self.hasMap["(ln(x)-avg)²"] = []

        for valores in self.hasMap["lg(Dxy)"]:
            self.hasMap["(ln(x)-avg)²"].append(decimal.Decimal(math.pow((valores-self.avg), 2)))

        for valores in self.hasMap["(ln(x)-avg)²"]:
            self.total_LogaritmoXY_AVG += valores

        self.variancia = self.total_LogaritmoXY_AVG / (len(self.hasMap["(ln(x)-avg)²"]) - 1)

    def calcular_Faixas_Log(self):
        self.faixasLOG["ln(PP)"] = decimal.Decimal(self.avg - (2*self.desvioPadrao))
        self.faixasLOG["ln(P)"] = decimal.Decimal(self.avg - (self.desvioPadrao))
        self.faixasLOG["ln(M)"] = decimal.Decimal(self.avg)
        self.faixasLOG["ln(G)"] = decimal.Decimal(self.avg + self.desvioPadrao)
        self.faixasLOG["ln(GG)"] = decimal.Decimal(self.avg + (2*self.desvioPadrao))

    def calcular_Faixas_Normal(self):
        self.faixasNORM["PP"] = (decimal.Decimal(math.e)) ** self.faixasLOG["ln(PP)"]
        self.faixasNORM["P"] = (decimal.Decimal(math.e)) ** self.faixasLOG["ln(P)"]
        self.faixasNORM["M"] = (decimal.Decimal(math.e)) ** self.faixasLOG["ln(M)"]
        self.faixasNORM["G"] = (decimal.Decimal(math.e)) ** self.faixasLOG["ln(G)"]
        self.faixasNORM["GG"] = (decimal.Decimal(math.e)) ** self.faixasLOG["ln(GG)"]

    def calcular_DesvioPadrao(self):
        self.desvioPadrao = decimal.Decimal(math.pow(self.variancia, 0.5))

    def ver_Faixas(self, hashMap):
        print("\nFaixas: ")
        for key in hashMap.keys():
            print("\tColuna <{}>: \t {}".format(key, hashMap[key]))

    def ver_resultados(self):
        print("Total Log: {}".format(self.total_LogaritmoXY))
        print("Media Log: {}".format(self.total_LogaritmoXY_AVG))
        print("Média M: {}".format(self.avg))
        print("Variância: {}".format(self.variancia))
        print("Desvio Padrão: {}".format(self.desvioPadrao))
        self.ver_Faixas(self.faixasLOG)
        self.ver_Faixas(self.faixasNORM)
