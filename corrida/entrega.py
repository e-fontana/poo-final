# Eduardo Lazarini Fontana
# Joao Victor Marques Kishimoto

from corrida import Corrida
from corrida.tipo_corrida import TipoCorrida
from endereco.rota import Rota
from cliente import Cliente

class Entrega(Corrida):
    def __init__(self, id: str, cliente: Cliente, rota: Rota) -> None:
        super().__init__(id, cliente, TipoCorrida.CARONA, rota)

    def __repr__(self):
        return super().__repr__()

    def calcular_valor_final(self, rota: Rota) -> None:
        if not rota.distancia:
            raise ValueError("Distancia nao definida")

        valorTotal = rota.distancia * 0.8

        self.set_valor_total = valorTotal