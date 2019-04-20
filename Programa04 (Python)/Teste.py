# -*- coding: utf-8 -*-

''' Universidade Federal do Parana - CM
    Engenharia de Software 02
    Renan Kodama Rodrigues 1602098
'''

from ClassCalcs import Calc
import collections
import decimal


def teste_Caso1():
    caso1 = collections.OrderedDict()
    caso1["Nome da parte"] = [
        "each_char","string_read","single_character",
        "each_line","single_char","string_builder",
        "string_manager", "list_clump", "list_clip",
        "string_decrementer", "Char", "Character","Converter"
        ]
    caso1["Tamanho da parte (LOC)"] = [18, 18, 25, 31, 37, 82, 82, 87, 89, 230, 85, 87, 558]
    caso1["Quantidade de Métodos"] = [3,3,3,3,3,5,4,4,4,10,3,3,10]
    resultado =  Calc(caso1).inicializar()

    assert round(resultado["PP"], 4) == round(decimal.Decimal(4.3953), 4)
    assert round(resultado["P"], 4) == round(decimal.Decimal(8.5081), 4)
    assert round(resultado["M"], 4) == round(decimal.Decimal(16.4696), 4)
    assert round(resultado["G"], 4) == round(decimal.Decimal(31.8811), 4)
    assert round(resultado["GG"], 4) == round(decimal.Decimal(61.7137), 4)


def teste_Caso2():
    caso2 = collections.OrderedDict()
    caso2["Capítulo"] = [
        "Preface", "Chapter 1", "Chapter 2", "Chapter 3",
        "Chapter 4", "Chapter 5", "Chapter 6", "Chapter 7",
        "Chapter 8", "Chapter 9", "Appendix", "Appendix A",
        "Appendix B", "Appendix C", "Appendix D", "Appendix E",
        "Appendix F"
        ]
    caso2["Quantidade de Páginas"] = [7, 12, 10, 12, 10, 12, 12, 12, 12, 8, 8, 8, 20, 14, 18, 12]
    resultado =  Calc(caso2).inicializar()

    assert round(resultado["PP"], 4) == round(decimal.Decimal(6.3375), 4)
    assert round(resultado["P"], 4) == round(decimal.Decimal(8.4393), 4)
    assert round(resultado["M"], 4) == round(decimal.Decimal(11.2381), 4)
    assert round(resultado["G"], 4) == round(decimal.Decimal(14.9650), 4)
    assert round(resultado["GG"], 4) == round(decimal.Decimal(19.9280), 4)
