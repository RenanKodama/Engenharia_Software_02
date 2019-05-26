# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Simpson import Simpson
from Simpson_Inv import SimpsonInv

class Calculos:
    def __init__(self, data_Hash, coluns, xk):
        self.data_Hash = data_Hash
        self.coluns = coluns
        self.size = len(self.data_Hash[self.coluns[0]])
        self.xk = xk
        self.seg = 1000

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
            v1.append(float(x))

        for y in self.data_Hash[self.coluns[1]]:
            v2.append(float(y))

        for i in range(len(v1)):
            x_y += v1[i] * v2[i]

        return x_y

    # recycled and changed
    def quadrado_XY(self):
        x_quadrado = 0
        y_quadrado = 0

        for x in self.data_Hash[self.coluns[0]]:
            x_quadrado += float(x) ** 2

        for y in self.data_Hash[self.coluns[1]]:
            y_quadrado += float(y) ** 2

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
        p = Simpson(0, x, (self.size - 2), num_seg=self.seg).calc()

        area_Tail = 1 - (2 * p)
        
        return [x, p, area_Tail]

    def intervalo_Previsao(self, x, beta_0, beta_1, avg_x, yk):
        [x, total_time]= SimpsonInv(x, self.size, 0.35, eRR=0.0001, num_seg=4).find_P()
        part1 = x * self.desvio_Padrao(beta_0, beta_1)
        part2l0_frac = (self.xk - avg_x) ** 2 
        part2l1_frac = 0

        for i in range (self.size):
            part2l1_frac += (float(self.data_Hash[self.coluns[0]][i]) - avg_x) ** 2

        part2 = (1 + (1 / self.size) + (part2l0_frac / part2l1_frac)) ** 0.5
        
        range_val =  part1 * part2

        return [range_val, (yk + range_val), (yk - range_val), total_time]

    def desvio_Padrao(self, beta_0, beta_1):
        part1 = (1 / (self.size - 2))
        part2 = 0
        vet1 = self.data_Hash[self.coluns[0]]
        vet2 = self.data_Hash[self.coluns[1]]

        for i in range(self.size):
            part2 += (float(vet2[i]) - beta_0 - (beta_1 * float(vet1[i]))) ** 2

        return ((part1 * part2) ** 0.5)

    def calcular(self):
        file_out = open("Output.txt", "w")

        x_y = self.multiplica_XY()
        [sum_x, sum_y] = self.somatorio_XY() 
        [x_quad, y_quad] = self.quadrado_XY()
        coef_corr = self.coeficiente_Correlacao(x_y, sum_x, sum_y, x_quad, y_quad)

        [x, p, area_Tail] = self.significancia_Correlacao(coef_corr)
        [avg_x, avg_y] = self.media_XY(sum_x, sum_y)
        [beta_0, beta_1] = self.regressao_Linear(x_y, avg_x, avg_y, x_quad)
        yk = self.encontrar_YK(beta_0, beta_1)

        [rang, upi, lpi, total_time] = self.intervalo_Previsao(x, beta_0, beta_1, avg_x, yk)
        
        file_out.write("Coef. Corr: {}".format(coef_corr))
        file_out.write("Coef. Corr²: {}".format(coef_corr ** 2))
        file_out.write("Area Tail: {}".format(area_Tail))
        file_out.write("Beta 0: {}".format(beta_0))
        file_out.write("Beta 1: {}".format(beta_1))
        file_out.write("YK: {}".format(yk))
        file_out.write("Range: {}".format(rang))
        file_out.write("Beta 0: {}".format(beta_0))
        file_out.write("Total Time: {} min".format(total_time))

        return [coef_corr, coef_corr ** 2, area_Tail, beta_0, beta_1, yk, rang, upi, lpi]