# !/usr/bin/python3
# encoding: ISO-8859-1
"""
Fun��o criada para testar a fun��o soma
"""
from src.main.soma import soma


def test_soma():
    """
    Testa a fun��o soma
    """
    result: int = soma(2, 3)
    assert result == 5
