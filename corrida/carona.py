from corrida import Corrida
from corrida.tipo_corrida import TipoCorrida
from endereco.rota import Rota

class Carona(Corrida):
    def __init__(self, id: str, cliente, valorOferecidoPorKm: float, rota: Rota) -> None:
        super().__init__(id, cliente, TipoCorrida.CARONA, rota)
        self.__valorOferecidoPorKm = valorOferecidoPorKm

    @property
    def valorOferecidoPorKm(self):
        return self.__valorOferecidoPorKm
    
    @valorOferecidoPorKm.setter
    def setValorOferecido(self, valor: float) -> None:
        if (valor < 0):
            raise ValueError("Valor nao pode ser negativo")

        self.__valorOferecidoPorKm = valor

    
    def valorFinalCorrida(self, rota: Rota) -> None:
        if not rota.distancia:
            raise ValueError("Distancia nao definida")

        valorTotal = rota.distancia * self.valorOferecidoPorKm

        self.valorTotal = valorTotal
        
