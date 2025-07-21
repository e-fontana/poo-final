# Eduardo Lazarini Fontana
# Joao Victor Marques Kishimoto

from corrida import Corrida
from endereco.rota import Rota
from corrida import TipoCorrida
from cliente import Cliente

class Ufber:
    def __init__(self):
        self.__historico_corridas: list[Corrida] = []
        self.__lista_rotas: list[Rota] = []
    
    def add_corrida(self, corrida: Corrida):
        self.__historico_corridas.append(corrida)
     
    def comecar_corrida(self, rota: Rota, corrida: Corrida):
        corrida.setRota = rota
        corrida.calcular_valor_total(rota)
    
    def comparar_corrida(self, corrida1: Corrida, corrida2: Corrida):
        return corrida1 == corrida2

    def adicionar_rota_com_distancia(self, origem: Rota, destino: Rota, distancia: float):
        rota = Rota(origem, destino)

        rota.set_distancia = distancia

        self.__lista_rotas.append(rota)
    
    def adicionar_rota(self, origem, destino):
        self.__lista_rotas.append(Rota(origem, destino))
                                  
    def resumo_corridas(self):
        for corrida in self.__historico_corridas:
            print(corrida)
