# Eduardo Lazarini Fontana
# Joao Victor Marques Kishimoto

from corrida import Corrida
from corrida.tipo_corrida import TipoCorrida
from endereco.rota import Rota
from cliente import Cliente

class Carona(Corrida):
    def __init__(self, id: str, cliente: Cliente, rota: Rota, valorOferecidoPorKm: float) -> None:
        super().__init__(id, cliente, TipoCorrida.CARONA, rota)
        self.__valorOferecidoPorKm = valorOferecidoPorKm

    def __repr__(self):
        return super().__repr__()

    @property
    def valorOferecidoPorKm(self):
        return self.__valorOferecidoPorKm
    
    @valorOferecidoPorKm.setter
    def setValorOferecido(self, valor: float) -> None:
        if (valor < 0):
            raise ValueError("Valor nao pode ser negativo")

        self.__valorOferecidoPorKm = valor

    
    def calcular_valor_final(self, rota: Rota) -> None:
        if not rota.distancia:
            raise ValueError("Distancia nao definida")

        valorTotal = rota.distancia * self.valorOferecidoPorKm

        self.set_valor_total = valorTotal
        
