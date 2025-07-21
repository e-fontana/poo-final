from endereco.endereco import Endereco

class Rota:
    def __init__(self, origem, destino):
        self.__origem = origem
        self.__destino = destino

    @classmethod
    def detailed(cls, origem: Endereco, destino: Endereco, distancia: float):
        return cls(origem, destino)

    @property
    def origem(self):
        return self.__origem
    @property
    def destino(self):
        return self.__destino
    @property
    def distancia(self):
        return self.__distancia
    
    @origem.setter
    def set_origem(self, origem):
        self.__origem = origem
    
    @destino.setter
    def set_destino(self, destino):
        self.__destino = destino
    
    @distancia.setter
    def set_distancia(self, distancia):
        self.__distancia = distancia