from typing import Final

class Cliente:
    def __init__(self, nome_completo: str, telefone: str, cpf: str):
        self.__nome_completo = nome_completo
        self.__telefone = telefone
        self.__cpf: Final = cpf
    
    @property
    def nome(self):
        return self.__nome_completo
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome_completo = nome
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone