# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import math

class Simpson:
    def __init__(self, x_init, x_final, eRR, dof, numSeg):
        self.x_init = x_init
        self.x = x_final
        self.eRR = eRR
        self.dof = dof
        self.numSeg = numSeg
        self.w = self.x / self.numSeg

    def calc(self):
        # print(self.func_Gamma(9.0))
        self.func_fX(9)

    def func_Gamma(self, value):
        if not value.is_integer():
            if math.isclose(value, (1/2)):
                return ((math.pi ** 0.5))
            else:
                return((value - 1) * self.func_Gamma((value - 1)))
        else:
            return self.func_GammaInt(value -1)

    def func_GammaInt(self, value):
        if value ==  1:
            return value
        else:
            return (value * self.func_GammaInt(value - 1))

    def func_fX(self, value):
        f_x_part1 = self.func_Gamma((self.dof + 1) / 2)
        f_x_part2 = ((self.dof * math.pi) ** 0.5) * self.func_Gamma(self.dof / 2)
        f_x_part3 = ((1+((value ** 2) / self.dof)) ** ((self.dof + 1) / 2)) 
        f_x_result = (f_x_part1 / f_x_part2) * f_x_part3
        
        print(f_x_part1)
        print(f_x_part2)
        print((f_x_part1 / f_x_part2))

    def func_Simpson(self):
        aux = 1