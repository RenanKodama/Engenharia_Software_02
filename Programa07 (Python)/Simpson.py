# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

import math


class Simpson:
    def __init__(self, x_init, x_final, dof, eRR=0.00001, num_seg=4):
        ''' Inicialização da classe Simpson.
            Parâmetros:
                x_init:
                    Tipo - Float.
                    Descrição - Representa o valor inicial de X
                x_final:
                    Tipo - Float.
                    Descrição - Representa o valor final de X
                dof:
                    Tipo - Integer.
                    Descrição - Valor de dof.
                eRR:
                    tipo - Float.
                    Descrição - Representa erro aceitável.
                num_seg:
                    Tipo - Integer.
                    Descrição - Representa o número de segmentos. Por
                        padrão é segmentos = 4.

            Retorno:
                Simpson
        '''
        self.x_init = x_init
        self.x = x_final
        self.eRR = eRR
        self.dof = dof
        self.num_seg = num_seg

    def calc(self):
        ''' Função para a converter o valor escolhido para o 
            valor estimado.

            Parâmetros:
                null

            Retorno:
                Retorna valor do tipo Float.
        '''
        old_val = self.func_Simpson()
        self.num_seg *= 2
        new_val = self.func_Simpson()

        while(abs(old_val - new_val) > self.eRR):
            self.num_seg *= 2
            old_val = new_val
            new_val = self.func_Simpson()

        return new_val

    def func_Gamma(self, value, perform = True):
        ''' Fatorial do valor passado por argumento.

            Parâmetros:
                value:
                    Tipo - Float.
                    Descrição - Representa o valor de entrada.
                perform:
                    Tipo - Boolean.
                    Descrição - Controle de performance. Se True
                        então use math.gamma(), caso contrário, use a
                        função implementada (mais lenta).

            Retorno:
                Retorna valor do tipo Float.
        '''
        if (perform):
            return math.gamma(float(value))
        else:
            if not float(value).is_integer():
                if math.isclose(value, (1 / 2)):
                    return ((math.pi ** 0.5))
                else:
                    return((value - 1) * self.func_Gamma((value - 1)))
            else:
                return self.func_GammaInt(value - 1)

    def func_GammaInt(self, value):
        ''' Fatorial do valor passado por argumento, do tipo integer.

            Parâmetros:
                value:
                    Tipo - Integer.
                    Descrição - Representa o valor de entrada.

            Retorno:
                Retorna valor do tipo Float.
        '''
        if value == 1:
            return value
        else:
            return (value * self.func_GammaInt(value - 1))

    def func_fX(self, value):
        '''Cálculo para FX(y).

            Parâmetros:
                value:
                    Tipo - Integer.
                    Descrição - Representa o valor de entrada.

            Retorno:
                Retorna valor do tipo Float.
        '''
        f_x_part1 = self.func_Gamma((self.dof + 1.0) / 2)
        f_x_part2 = (
            ((self.dof * math.pi) ** 0.5) * self.func_Gamma(self.dof / 2.0)
            )
        f_x_part3 = (
            ((1.0 + ((value ** 2.0) / self.dof)) ** - ((self.dof + 1.0) / 2.0))
            )
        f_x_result = (f_x_part1 / f_x_part2) * f_x_part3

        return f_x_result

    def func_Simpson(self):
        '''Cálculo para FX(y).

            Parâmetros:
                null.

            Retorno:
                Retorna valor do tipo Float.
        '''
        var_W = self.x / self.num_seg
        var_P_part1 = self.func_fX(0.0)
        var_P_part2 = 0.0
        var_P_part3 = 0.0
        var_P_part4 = self.func_fX(self.x)
        var_P_part2 += sum(4.0 * self.func_fX(var_W * i) for i in range(1, self.num_seg - 1, 2))
        var_P_part3 += sum(2.0 * self.func_fX(var_W * i) for i in range(2, self.num_seg - 2, 2))

        var_P_result = (
            (var_W / 3) *
            (var_P_part1 + var_P_part2 + var_P_part3 + var_P_part4)
            )

        return var_P_result
