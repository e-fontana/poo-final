# Eduardo Lazarini Fontana
# Joao Victor Marques Kishimoto

from corrida import Corrida
from endereco.rota import Rota
from corrida import TipoCorrida
from cliente import Cliente

class Ufber:
    def __init__(self):
        self.__historico_corridas: list[Corrida] = []
        self.__lista_trajetos: list[Rota] = []
    
    def add_corrida(self, corrida: Corrida):
        self.__historico_corridas.append(corrida)
     
    def comecar_corrida(self, rota, corrida):
        corrida.setRota(rota)
        corrida.calcular_valor_corrida(rota)

    
    def comparar_corrida(self, corrida1: Corrida, corrida2: Corrida):
        return corrida1 == corrida2

    def adicionar_trajeto_com_distancia(self, origem: Rota, destino: Rota, distancia: float):
        rota = Rota(origem, destino)
        rota.set_distancia = distancia

    def adicionar_rota(self, origem, destino, distancia):
        self.__lista_rotas.append(Rota(origem, destino, distancia))
    
    def adicionar_rota(self, origem, destino):
        self.__lista_rotas.append(Rota(origem, destino))
