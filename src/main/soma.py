# !/usr/bin/python3
# encoding: ISO-8859-1
"""Função criada para somar dois números."""


def soma(num_1: int, num_2: int) -> int:
    """
    Retorna a soma de dois números.

    Parameters
        :param num_1: Primeiro Numero da Soma
        :type num_1: int
        :param num_2: Segundo Numero da Soma
        :type num_2: int

    Returns
        :return soma_dois_numeros: Soma dos dois números
        :rtype soma_dois_numeros: int

    Exemples:
        >>> num_3 = 1
        >>> num_4 = 2
        >>> soma(num_1, num_2)
        3

    """
    soma_dois_numeros: int = num_1 + num_2
    return soma_dois_numeros
