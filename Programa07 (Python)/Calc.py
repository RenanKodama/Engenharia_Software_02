# -*- coding: utf-8 -*-

''' Universidade Tecnológica Federal do Paraná - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from Simpson import Simpson
from Simpson_Inv import SimpsonInv


class Calculos:
    def __init__(self, data_Hash, coluns, xk, seg=2):
        ''' Inicialização da classe Calculos.
            Parâmetros:
                data_Hash:
                    Tipo - Dict {}.
                    Descrição - Representa os dados
                        contidos nas tabelas. Onde Keys =
                        identifacadores das colunas e
                        Key[value] = os dados presentes nas colunas. 
                coluns:
                    Tipo - list [] de strings.
                    Descrição - Representa as colunas
                        selecionadas para os cálculos.
                xk:
                    Tipo - Integer.
                    Descrição - Valor de XK.
                seg:
                    Tipo - Integer.
                    Descrição - Representa o número de segmentos. Por
                        padrão é segmentos = 2.

            Retorno:
                Calculos
        '''
        self.data_Hash = data_Hash
        self.coluns = coluns
        self.size = 0
        self.xk = xk
        self.seg = seg

    # recycled and changed
    def somatorio_XY(self):
        ''' Cálculo para o somatório dos valores contidos
            nos dados das tabelas para as colunas X e Y
            selecionadas.

            Parâmetros:
                null.

            Retorno:
                Retorna lista do tipo float de tamanho = 2.
                    list[0] = Soma dos valores em X.
                    list[1] = Soma dos valores em Y.
        '''
        sum_x = 0
        sum_y = 0

        for x in self.data_Hash[self.coluns[0]]:
            sum_x += float(x)

        for y in self.data_Hash[self.coluns[1]]:
            sum_y += float(y)

        return [sum_x, sum_y]

    # recycled and changed
    def multiplica_XY(self):
        ''' Cálculo da soma dos produtos entre os valores contidos
            nos dados das tabelas para as colunas X e Y
            selecionadas.

            Parâmetros:
                null.

            Retorno:
                Retorna valor do tipo Float.
        '''
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
        ''' Cálculo da soma dos quadrados para os valores 
            contidos nos dados das tabelas nas colunas X e Y
            selecionadas.

            Parâmetros:
                null.

            Retorno:
                Retorna lista do tipo float de tamanho = 2.
                list[0] = Soma dos valores² em X.
                list[1] = Soma dos valores² em Y.
        '''
        x_quadrado = 0
        y_quadrado = 0

        for x in self.data_Hash[self.coluns[0]]:
            x_quadrado += float(x) ** 2

        for y in self.data_Hash[self.coluns[1]]:
            y_quadrado += float(y) ** 2

        return [x_quadrado, y_quadrado]

    # recycled and changed
    def media_XY(self, sum_X, sum_Y):
        ''' Cálculo da média entre os valores contidos 
            nos dados das tabelas para as colunas X e Y
            selecionadas.

            Parâmetros:
                sum_X:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores para a coluna X.
                sum_Y:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores para a coluna Y.

            Retorno:
                Retorna lista do tipo float de tamanho = 2.
                list[0] = Média dos valores em X.
                list[1] = Média dos valores em Y.
        '''
        avg_x = (sum_X) / self.size
        avg_y = (sum_Y) / self.size

        return [avg_x, avg_y]

    # recycled and changed
    def coeficiente_Correlacao(self, x_y, sum_X, sum_Y, x_quad, y_quad):
        ''' Cálculo do coeficiente de correlação entre os dados
            presentes nas colunas X e Y selecionadas.

            Parâmetros:
                x_y:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        produtos entre as colunas X e Y.
                sum_X:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores para a coluna X.
                sum_Y:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores para a coluna Y.
                x_quad:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores ao quadrado em X.
                                x_quad:
                y_quad:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores ao quadrado em X.

            Retorno:
                Retorna lista do tipo float de tamanho = 2.
                list[0] = Média dos valores em X.
                list[1] = Média dos valores em Y.
        '''
        part1 = (self.size * x_y) - (sum_X * sum_Y)
        part2 = (
            ((self.size * x_quad) - (sum_X ** 2)) *
            ((self.size * y_quad) - (sum_Y ** 2))
            )

        return (part1 / (part2 ** 0.5))

    # recycled and changed
    def regressao_Linear(self, x_y, avg_X, avg_Y, x_quad):
        ''' Cálculo para a regressão linear entre os dados
            presentes nas colunas X e Y selecionadas.

            Parâmetros:
                x_y:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        produtos entre as colunas X e Y.
                avg_X:
                    Tipo - Float.
                    Descrição - Representa a média entre
                        os valores da coluna X.
                avg_Y:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores para a coluna Y.
                x_quad:
                    Tipo - Float.
                    Descrição - Representa a soma dos
                        valores ao quadrado em X.
                                x_quad:

            Retorno:
                Retorna lista do tipo float de tamanho = 2.
                list[0] = Valor de beta 0.
                list[1] = Valor de beta 1.
        '''
        beta_1 = (
            (x_y - (self.size * avg_X * avg_Y)) /
            (x_quad - (self.size * (avg_X * avg_X)))
            )
        beta_0 = avg_Y - (beta_1 * avg_X)

        return [beta_0, beta_1]

    def encontrar_YK(self, beta_0, beta_1):
        ''' Cálculo para encontrar valor de YK entre os 
            dados presentes nas colunas X e Y selecionadas.

            Parâmetros:
                beta_0:
                    Tipo - Float.
                    Descrição - Representa o valor para
                        beta 0, podendo ser obtida pela 
                        regressão linear.
                                    beta_0:
                beta_1:
                    Tipo - Float.
                    Descrição - Representa o valor para
                        beta 1, podendo ser obtida pela 
                        regressão linear.

            Retorno:
                Retorna valor do tipo Float.
        '''
        return (beta_0 + (beta_1 * self.xk))

    def significancia_Correlacao(self, val_corr):
        ''' Cálculo para encontrar a significância 
            da correlação entre os dados presentes 
            nas colunas X e Y selecionadas.

            Parâmetros:
                val_corr:
                    Tipo - Float.
                    Descrição - Representa o valor do
                        coeficiente de correlação 
                        entre as colunas X e Y.

            Retorno:
                Retorna lista do tipo float de tamanho = 3.
                list[0] = Valor de x.
                list[1] = Valor de p.
                list[2] = Valor da área da cauda.
        '''
        part1 = abs(val_corr) * ((self.size - 2) ** (0.5))
        part2 = (1 - (val_corr ** 2)) ** 0.5
        x = part1 / part2
        p = Simpson(
            0, x, (self.size - 2), num_seg=self.seg
            ).calc()

        area_Tail = 1 - (2 * p)

        return [x, p, area_Tail]

    def intervalo_Previsao(self, x, beta_0, beta_1, avg_x, yk):
        ''' Cálculo para encontrar o intervalo de 
            previsão entre os dados presentes 
            nas colunas X e Y selecionadas.

            Parâmetros:
                x:
                    Tipo - Float.
                    Descrição - Representa o valor de X.
                beta_0:
                    Tipo - Float.
                    Descrição - Representa o valor de beta_0.
                beta_1:
                    Tipo - Float.
                    Descrição - Representa o valor de beta 1.
                avg_x:
                    Tipo: Float.
                    Descrição - Representa o valor da média em X.
                yk:
                    tipo: Float.
                    Descrição - Representa o valor de yk.

            Retorno:
                Retorna lista do tipo float de tamanho = 4.
                list[0] = Valor de range.
                list[1] = Valor de UPI.
                list[2] = Valor de LPI.
                list[3] = Total de tempo gasto.
        '''
        [x, total_time] = SimpsonInv(
            x, self.size - 2, 0.35, eRR=0.001, num_seg=2
            ).find_P()
        part1 = x * self.desvio_Padrao(beta_0, beta_1)
        part2l0_frac = (self.xk - avg_x) ** 2
        part2l1_frac = 0

        for i in range(self.size):
            part2l1_frac += (
                float(self.data_Hash[self.coluns[0]][i]) - avg_x
                ) ** 2

        part2 = (
            1 + (1 / self.size) + (part2l0_frac / part2l1_frac)
            ) ** 0.5

        range_val = part1 * part2

        return [range_val, (yk + range_val), (yk - range_val), total_time]

    def desvio_Padrao(self, beta_0, beta_1):
        ''' Cálculo para encontrar o desvio padrão
            entre os dados presentes nas colunas 
            X e Y selecionadas.

            Parâmetros:
                beta_0:
                    Tipo - Float.
                    Descrição - Representa o valor de beta_0.
                beta_1:
                    Tipo - Float.
                    Descrição - Representa o valor de beta 1.

            Retorno:
                Retorna valor do tipo Float.
        '''
        part1 = (1 / (self.size - 2))
        part2 = 0
        vet1 = self.data_Hash[self.coluns[0]]
        vet2 = self.data_Hash[self.coluns[1]]

        for i in range(self.size):
            part2 += (
                float(vet2[i]) - beta_0 - (beta_1 * float(vet1[i]))
                ) ** 2

        return ((part1 * part2) ** 0.5)

    def check_Data(self):
        ''' Função para checar a integridade dos dados inseridos.

            Parâmetros:
                null.

            Exceções:
                ValueError
                    Coluna X não encontrada!
                        Causa: Coluna passada por parâmetro não
                            encontrada nos dados.

                    Tamanhos das colunas diferem!
                        Causa: A quantidade de dados presentes nas
                            colunas dos dados, estão com quantidades
                            diferentes.

                    Número de segmentos deve ser par e > 0 obteve: X!
                        Causa: Valor para o número de seguimentos é menor
                            que ou igual à zero ou o número de segmentos
                            é impar.

                    Duas colunas devem ser selecionadas!
                        Causa: Número de colunas inseridas é diferente de 2.

            Retorno:
                null.
        '''
        for col in self.coluns:
            if col not in self.data_Hash.keys():
                raise ValueError("Coluna '{}' não encontrada!".format(col))

        count_itens = []
        for key in self.data_Hash.keys():
            count_itens.append(self.data_Hash[key].count())

        if len(self.coluns) != 2:
            raise ValueError("Duas colunas devem ser selecionadas!")

        if not all(
            size_col == self.data_Hash.shape[0] for size_col in count_itens):
                raise ValueError("Tamanhos das colunas diferem!")

        self.size = len(self.data_Hash[self.coluns[0]])
        if ((self.seg % 2) != 0) or (self.seg <= 0):
            raise ValueError(
                "Número de segmentos deve ser par e > 0 obteve: '{}'!".format(
                    self.seg))

    def calcular(self):
        ''' Função inicializar os calculos para encontrar uma estivamativa
            melhorada.

            Parâmetros:
                null.

            Retorno:
                Retorna lista do tipo float de tamanho = 10.
                list[0] = Coeficiente de Correlação.
                list[1] = Coeficiente de Correlação².
                list[2] = Área da Cauda.
                list[3] = Beta 0.
                list[4] = Beta 1.
                list[5] = YK.
                list[6] = Range.
                list[7] = UPI.
                list[8] = LPI.
                list[9] = Total de tempo gasto.

                Arquivo de sáida como Output.csv em 
                ./Programa07/ .Contendo os valores da 
                lista de retorno de calcular().
        '''
        self.check_Data()
        file_out = open("Output.csv", "w")

        x_y = self.multiplica_XY()
        [sum_x, sum_y] = self.somatorio_XY()
        [x_quad, y_quad] = self.quadrado_XY()
        coef_corr = self.coeficiente_Correlacao(
            x_y, sum_x, sum_y, x_quad, y_quad
            )

        [x, p, area_Tail] = self.significancia_Correlacao(coef_corr)
        [avg_x, avg_y] = self.media_XY(sum_x, sum_y)
        [beta_0, beta_1] = self.regressao_Linear(x_y, avg_x, avg_y, x_quad)
        yk = self.encontrar_YK(beta_0, beta_1)

        [rang, upi, lpi, 
        total_time] = self.intervalo_Previsao(x, beta_0, beta_1, avg_x, yk)

        file_out.write("Coef. Corr: {}\n".format(coef_corr))
        file_out.write("Coef. Corr²: {}\n".format(coef_corr ** 2))
        file_out.write("Area Tail: {}\n".format(area_Tail))
        file_out.write("Beta 0: {}\n".format(beta_0))
        file_out.write("Beta 1: {}\n".format(beta_1))
        file_out.write("YK: {}\n".format(yk))
        file_out.write("Range: {}\n".format(rang))
        file_out.write("Beta 0: {}\n".format(beta_0))
        file_out.write("Total Time: {} min\n".format(total_time))

        print("Resultados exportados para ./Output.csv")

        return [
            coef_corr, coef_corr ** 2, area_Tail,
            beta_0, beta_1, yk, rang, upi, lpi, total_time
            ]
