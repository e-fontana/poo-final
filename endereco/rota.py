from endereco import Endereco
class Rota:
    def __init__(self, origem: Endereco, destino: Endereco, distancia: float):
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia

    def __init__(self, origem, destino):
        self.__origem = origem
        self.__destino = destino

    def get_origem(self):
        return self.__origem
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    
    def set_origem(self, origem):
        self.__origem = origem
    def set_destino(self, destino):
        self.__destino = destino
    def set_distancia(self, distancia):
        self.__distancia = distancia