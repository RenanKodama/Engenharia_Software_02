# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import math
import time


class Simpson:
    def __init__(self, x, dof, p, eRR = 0.00001, num_seg = 100):
        self.x = x
        self.eRR = eRR
        self.dof = dof
        self.num_seg = num_seg
        self.p = p
        self.d = 0.5

    def calc(self):
        old_val = self.func_Simpson()
        self.num_seg *= 2
        new_val = self.func_Simpson()

        while((old_val - new_val) > self.eRR):
            self.num_seg *= 2
            old_val = new_val
            new_val = self.func_Simpson()

        return new_val

    def func_Gamma(self, value):
        if not float(value).is_integer():
            if math.isclose(value, (1 / 2)):
                return ((math.pi ** 0.5))
            else:
                return((value - 1) * self.func_Gamma((value - 1)))
        else:
            return self.func_GammaInt(value - 1)

    def func_GammaInt(self, value):
        if value == 1:
            return value
        else:
            return (value * self.func_GammaInt(value - 1))

    def func_fX(self, value):
        f_x_part1 = self.func_Gamma((self.dof + 1.0) / 2)
        f_x_part2 = (
            ((self.dof * math.pi) ** 0.5) * self.func_Gamma(self.dof / 2.0)
            )
        f_x_part3 = (
            ((1.0 + ((value ** 2.0) / self.dof)) ** -((self.dof + 1.0) / 2.0))
            )
        f_x_result = (f_x_part1 / f_x_part2) * f_x_part3

        return f_x_result

    def func_Simpson(self):
        var_W = self.x / self.num_seg
        var_P_part1 = self.func_fX(0.0)
        var_P_part2 = 0.0
        var_P_part3 = 0.0
        var_P_part4 = self.func_fX(self.x)

        for i in range(1, self.num_seg - 1, 2):
            var_P_part2 += (4.0 * self.func_fX(i * var_W))

        for i in range(2, self.num_seg - 2, 2):
            var_P_part3 += (2.0 * self.func_fX(i * var_W))

        var_P_result = (
            (var_W / 3) *
            (var_P_part1 + var_P_part2 + var_P_part3 + var_P_part4)
            )

        return var_P_result

    def find_P(self):
        time_init = time.clock()
        result = self.calc()
        positive = self.is_Positive(self.p - result)

        while(not math.isclose(self.p, result, rel_tol=self.eRR)):
            if result < self.p:
                self.x += self.d
            else:
                self.x -= self.d

            result = self.calc()

            # print("Val_X: {}".format(self.x))

            if (self.is_Positive(self.p - result) != positive):
                positive = self.is_Positive(self.p - result)
                self.d /= 2

        time_final = time.clock()
        print("Time: ".format(time_final - time_init))
        return self.x

    def is_Positive(self, number):
        if(number > 0):
            return True
        else:
            return False

