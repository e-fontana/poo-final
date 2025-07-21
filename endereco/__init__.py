# Eduardo Lazarini Fontana
# Joao Victor Marques Kishimoto

class Endereco:
    def __init__(self, nome, rua, numero, bairro):
        self.__nome = nome
        self.__rua = rua
        self._numero = numero
        self.__bairro = bairro
    def get_nome(self):
        return self.__nome
    def get_rua(self):
        return self.__rua
    def get_numero(self):
        return self.__numero
    def get_bairro(self):
        return self.__bairro
    def set_nome(self, nome):
        self.__nome = nome
    def set_rua(self, rua):
        self.__rua = rua
    def set_numero(self, numero):
        self.__numero = numero
    def set_bairro(self, bairro):
        self.__bairro = bairro