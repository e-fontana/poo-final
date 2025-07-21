# Eduardo Lazarini Fontana
# Joao Victor Marques Kishimoto

from corrida import Corrida
from endereco.rota import Rota

class Ufber:
    def __init__(self):
        self.__historico_corridas: list[Corrida] = []
        self.__lista_trajetos: list[Rota] = []
    
    def add_corrida(self, corrida: Corrida):
        self.__historico_corridas.append(corrida)

    def comecar_corrida(self, rota: Rota, corrida: Corrida):
        corrida.setRota = rota
        corrida.calcular_valor_final(rota)
    
    def comparar_corrida(self, corrida1: Corrida, corrida2: Corrida):
        return corrida1 == corrida2

    def adicionar_trajeto_com_distancia(self, origem: Rota, destino: Rota, distancia: float):
        rota = Rota(origem, destino)
        rota.set_distancia = distancia

        self.__lista_trajetos.append(rota)
    
    def adicionar_trajeto(self, origem: Rota, destino: Rota):
        self.__lista_trajetos.append(Rota(origem, destino))