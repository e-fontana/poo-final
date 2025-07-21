from corrida import Corrida
from corrida.tipo_corrida import TipoCorrida
from endereco import Rota

class Carona(Corrida):
    def __init__(self, id: str, cliente) -> None:
        super().__init__(id, cliente, TipoCorrida.CARONA)

    def valorFinalCorrida(rota):
        pass