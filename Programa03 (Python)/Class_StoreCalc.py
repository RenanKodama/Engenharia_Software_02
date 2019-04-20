# -*- coding: utf-8 -*-

''' Universidade Federal do Parana - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import decimal
import collections


class StoreCalc:
    def __init__(self, hashMap, xk):
        self.sum_x = decimal.Decimal(0)
        self.sum_y = decimal.Decimal(0)
        self.avg_x = decimal.Decimal(0)
        self.avg_y = decimal.Decimal(0)
        self.x_quadrado = decimal.Decimal(0)
        self.y_quadrado = decimal.Decimal(0)
        self.x_y = decimal.Decimal(0)
        self.beta_1 = decimal.Decimal(0)
        self.beta_0 = decimal.Decimal(0)
        self.r_xy = decimal.Decimal(0)
        self.r_quadrado = decimal.Decimal(0)
        self.yk = decimal.Decimal(0)
        self.xk = xk
        self.hashMap = hashMap
        self.key1 = list(self.hashMap.keys())[1]
        self.key2 = list(self.hashMap.keys())[2]

    def inicializar(self):
        self.somatorio_XY()
        self.quadrado_XY()
        self.media_XY()
        self.multiplica_XY()
        self.calculo_Beta01()
        self.coeficiente_Correlacao()
        self.encontrar_YK()
        self.resultados()
        return self

    def somatorio_XY(self):
        for x in self.hashMap[self.key1]:
            self.sum_x += decimal.Decimal(x)

        for y in self.hashMap[self.key2]:
            self.sum_y += decimal.Decimal(y)

    def media_XY(self):
        self.avg_x = decimal.Decimal(self.sum_x) / len(self.hashMap[self.key1])
        self.avg_y = decimal.Decimal(self.sum_y) / len(self.hashMap[self.key2])

    def quadrado_XY(self):
        for x in self.hashMap[self.key1]:
            self.x_quadrado += (decimal.Decimal(x) * decimal.Decimal(x))

        for y in self.hashMap[self.key2]:
            self.y_quadrado += (decimal.Decimal(y) * decimal.Decimal(y))

    def multiplica_XY(self):
        v1 = []
        v2 = []

        for x in self.hashMap[self.key1]:
            v1.append(decimal.Decimal(x))

        for y in self.hashMap[self.key2]:
            v2.append(decimal.Decimal(y))

        if len(v1) == len(v2):
            for i in range(len(v1)):
                self.x_y += v1[i] * v2[i]
        else:
            print("Erro Nº de Colunas Diferentes!")

    def calculo_Beta01(self):
        tam_n = decimal.Decimal(len(self.hashMap[self.key1]))
        self.beta_1 = (
            (self.x_y - (tam_n * self.avg_x * self.avg_y)) /
            (self.x_quadrado - (tam_n * (self.avg_x * self.avg_x)))
            )
        self.beta_0 = self.avg_y - (self.beta_1 * self.avg_x)

    def coeficiente_Correlacao(self):
        tam_n = decimal.Decimal(len(self.hashMap[self.key1]))
        part1 = (tam_n * self.x_y) - (self.sum_x * self.sum_y)
        part2 = (
            ((tam_n * self.x_quadrado) - (self.sum_x ** 2)) *
            ((tam_n * self.y_quadrado) - (self.sum_y ** 2))
            )
        self.r_xy = part1 / (part2 ** decimal.Decimal(0.5))
        self.r_quadrado = self.r_xy ** 2

    def encontrar_YK(self):
        self.yk = self.beta_0 + (self.beta_1 * self.xk)

    def resultados(self):
        print("Somatorio_X <{}>: {}".format(self.key1, self.sum_x))
        print("Somatorio_Y <{}>: {}".format(self.key2, self.sum_y))
        print("X² <{}>: {}".format(self.key1, self.x_quadrado))
        print("Y² <{}>: {}".format(self.key2, self.y_quadrado))
        print("Média_X <{}>: {}".format(self.key1, self.avg_x))
        print("Média_Y <{}>: {}".format(self.key2, self.avg_y))
        print("Somatorio_X*Y <{}|{}>: {}".format(
            self.key1, self.key2, self.x_y))
        print("Beta 1: {}".format(self.beta_1))
        print("Beta 0: {}".format(self.beta_0))
        print("Coef. Corr.: {}".format(self.r_xy))
        print("Coef. Corr.²: {}".format(self.r_quadrado))
        print("YK: {}\n\n".format(self.yk))
