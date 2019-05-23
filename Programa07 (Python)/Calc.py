# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Simspon import Simspon


class Caculos:
    def __init__(self, data_Hash, coluns, xk):
        self.data_Hash = data_Hash
        self.coluns = coluns
        self.size = len(self.data_Hash[self.coluns[0]])
        self.xk = xk

    # recycled and changed
    def somatorio_XY(self):
        sum_x = 0
        sum_y = 0

        for x in self.data_Hash[self.coluns[0]]:
            sum_x += float(x)

        for y in self.data_Hash[self.coluns[1]]:
            sum_y += float(y)

        return [sum_x, sum_y]

    # recycled and changed
    def multiplica_XY(self):
        v1 = []
        v2 = []
        x_y = 0

        for x in self.data_Hash[self.coluns[0]]:
            v1.append((x))

        for y in self.data_Hash[self.coluns[1]]:
            v2.append((y))

        for i in range(len(v1)):
            x_y += v1[i] * v2[i]

        return x_y

    # recycled and changed
    def quadrado_XY(self):
        x_quadrado = 0
        y_quadrado = 0

        for x in self.data_Hash[self.coluns[0]]:
            x_quadrado += (x * x)

        for y in self.data_Hash[self.coluns[1]]:
            y_quadrado += (y * y)

        return [x_quadrado, y_quadrado]

    # recycled and changed
    def media_XY(self, sum_x, sum_y):
        avg_x = (sum_x) / len(self.data_Hash[self.coluns[0]])
        avg_y = (sum_y) / len(self.data_Hash[self.coluns[1]])

        return [avg_x, avg_y]

    # recycled and changed
    def coeficiente_Correlacao(self, x_y, sum_x, sum_y, x_quad, y_quad):
        part1 = (self.size * x_y) - (sum_x * sum_y)
        part2 = (
            ((self.size * x_quad) - (sum_x ** 2)) *
            ((self.size * y_quad) - (sum_y ** 2))
            )

        return (part1 / (part2 ** 0.5))

    # recycled and changed
    def regressao_Linear(self, x_y, avg_x, avg_y, x_quad):
        beta_1 = (
            (x_y - (self.size * avg_x * avg_y)) /
            (x_quad - (self.size * (avg_x * avg_x)))
            )
        beta_0 = avg_y - (beta_1 * avg_x)

        return [beta_0, beta_1]
    
    def encontrar_YK(self, beta_0, beta_1):
        return (beta_0 + (beta_1 * self.xk))

    def significancia_Correlacao(self, val_corr):
        part1 = abs(val_corr) * ((self.size - 2) ** (0.5))
        part2 = (1 - (val_corr ** 2)) ** 0.5
        x = part1 / part2
        p = Simspon(0, x, (self.size - 2))
        
        # return (part1 / part2)


    def calcular(self):
        x_y = multiplica_XY()
        [sum_x, sum_y] = somatorio_XY() 
        [x_quad, y_quad] = quadrado_XY()
        coef_corr = coeficiente_Correlacao(x_y, sum_x, sum_y, x_quad, y_quad)

        # sign_Corr = significancia_Correlacao(coef_corr)

        [avg_x, avg_y] = media_XY(sum_x, sum_y)
        [beta_0, beta_1] = regressao_Linear(x_y, avg_x, avg_y, x_quad)
        yk = encontrar_YK(beta_0, beta_1)
