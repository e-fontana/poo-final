from corrida import Corrida
from endereco.rota import Rota
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
        return corrida1 == corrida2

    def adicionar_trajeto_com_distancia(self, origem, destino, distancia):
        rota = Rota(origem, destino)
        rota.set_distancia = distancia

        self.__lista_trajetos.append(rota)
    
    def adicionar_trajeto(self, origem, destino):
        self.__lista_trajetos.append(Rota(origem, destino))