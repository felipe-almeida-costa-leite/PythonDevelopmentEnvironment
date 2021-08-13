# !/usr/bin/python3
# encoding: ISO-8859-1
"""
Função criada para testar a função soma
"""
from src.main.soma import soma


def test_soma():
    """
    Testa a função soma
    """
    result: int = soma(2, 3)
    assert result == 5
