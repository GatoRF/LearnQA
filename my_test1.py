import pytest
import requests



class TestMy():
    def test_lenworld(self):
        phrase = input("Set a phrase: ")
        ddd = len(phrase)
        assert ddd < 15, f'phrase {ddd} > 15'

