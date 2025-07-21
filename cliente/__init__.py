from typing import Final
from corrida import Corrida

class Cliente:
    def __init__(self, nome_completo: str, telefone: str, cpf: str):
        self.__nome_completo = nome_completo
        self.__telefone = telefone
        self.__cpf: Final = cpf
        self.__historico_corridas = []
    
    def get_nome(self):
        return self.__nome_completo
    
    def get_telefone(self):
        return self.__telefone
    
    def get_cpf(self):
        return self.__cpf

    def set_nome(self, nome):
        self.__nome_completo = nome
    
    def set_telefone(self, telefone):
        self.__telefone = telefone

    def add_corrida(self, corrida):
        self.__historico_corridas.append(corrida);