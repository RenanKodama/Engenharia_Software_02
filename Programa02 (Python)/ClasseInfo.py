# -*- coding: utf-8 -*-

''' Universidade Federal do Parana - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from ClasseMap import ClasseMap

import re


class ClasseInfo:
    def __init__(self, arquivo):
        self.countTotalLines = 0
        self.countLinhasUteis = 0
        self.arquivo = arquivo.readlines()
        self.map = dict()
        self.numSpaces = 4

    def countLines(self):
        for linha in self.arquivo:
            self.countTotalLines += 1

            if linha.find("\n"):
                self.countLinhasUteis += 1

    def countLinesNoCommentNoEmpty(self):
        expression_NOTEMPTY = re.compile(r"[[A-Za-z]+.[\(|)]*]*")
        expression_COMMENT = re.compile(r"((^\s)*(#).*)")

        numLines = 0
        for linha in self.arquivo:
            if (not expression_COMMENT.findall(
                    linha) and expression_NOTEMPTY.findall(linha)):
                numLines += 1
        return numLines

    def countTabs(self, linha):
        expression = re.compile(r"^\s+")
        somaTab = 0

        for tab in expression.findall(linha):
            somaTab += len(tab)
        return somaTab

    def concatEscopo(self, escopo):
        escopoMap = ""

        for identacao in escopo:
                escopoMap = escopoMap+"-"+identacao

        return escopoMap

    def countClass(self):
        expression_DEF = re.compile(r"[^\s]?def [\w]*[(]")
        expression_CLASS = re.compile(r"^[\w]*class [A-Za-z]*")
        expression_NOTEMPTY = re.compile(r"[[A-Za-z]+.[\(|)]*]*")
        expression_COMMENT = re.compile(r"((^\s)*(#).*)")
        escopo = ["Principal"]
        numTabs = 0
        self.map[self.concatEscopo(escopo)] = ClasseMap()

        for linha in self.arquivo:

            if expression_NOTEMPTY.findall(linha) and not(
                    expression_COMMENT.findall(linha)):

                if(expression_CLASS.findall(linha)):
                    escopo.append(expression_CLASS.findall(
                        linha)[0].split(" ")[1])
                    self.map[self.concatEscopo(escopo)] = ClasseMap()
                    numTabs = self.countTabs(linha)

                elif(expression_DEF.findall(linha)):
                    if(self.countTabs(linha) > numTabs):
                        numTabs = self.countTabs(linha)
                        escopo.append(expression_DEF.findall(
                            linha)[0].split(" ")[1].replace("(", ""))
                        self.map[self.concatEscopo(escopo)] = ClasseMap()
                    else:
                        if(escopo.pop().__eq__("Principal")):
                            escopo.append("Principal")

                        numTabs = self.countTabs(linha)
                        escopo.append(expression_DEF.findall(
                            linha)[0].split(" ")[1].replace("(", ""))
                        self.map[self.concatEscopo(escopo)] = ClasseMap()

                for palavra in linha.split(" "):
                    self.map.get(self.concatEscopo(
                        escopo)).getItens().append(palavra)

    def setCountTotalLines(self, valor):
        self.countTotalLines = valor

    def getCountTotalLines(self):
        return self.countTotalLines

    def setCountLinhasUteis(self, valor):
        self.countLinhasUteis = valor

    def getCountLinhasUteis(self):
        return self.countLinhasUteis

    def verResultados(self):
        print("Total de Linhas: {}".format(self.countTotalLines))
        print("Total de Linhas não Vazias: {}".format(self.countLinhasUteis))
        print("Total de Linhas Vazias e Sem Comentarios: {}\n".format(
            self.countLinesNoCommentNoEmpty()))

        print("Quantidade de Itens por Função {")
        for key in self.map.keys():
            print("\tFunção<{}>: {}".format(key, len(
                self.map[key].getItens())))
        print("}\n")

        print("Itens por Função: {")
        for key in self.map.keys():
            print("\tFunção<{}> \n\t".format(key)),

            for values in self.map[key].getItens():
                print(" {}".format(values)),

            print("---------------------------------------------------")
        print("}")
