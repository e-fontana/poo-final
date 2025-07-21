from corrida import Corrida
from endereco.tora import Rota
from corrida import TipoCorrida
from cliente import Cliente

class Ufber:
    def __init__(self):
        self.__historico_corridas = []
        self.__lista_trajetos = []
    
    def add_corrida(self, corrida):
        self.__historico_corridas.append(corrida)

    def comecar_corrida(self, rota, corrida):
        corrida.setRota(rota)
        corrida.calcular_valor_corrida(rota)

    
    def comparar_corrida(self, corrida1, corrida2):
        if corrida1 == corrida2: return True
        else: return False

    def adicionar_rota(self, origem, destino, distancia):
        self.__lista_rotas.append(Rota(origem, destino, distancia))
    
    def adicionar_rota(self, origem, destino):
        self.__lista_rotas.append(Rota(origem, destino))