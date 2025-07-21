from corrida import Corrida
from corrida.tipo_corrida import TipoCorrida
from endereco.rota import Rota

class Prolabore(Corrida):
    def __init__(self, id: str, cliente, rota: Rota) -> None:
        super().__init__(id, cliente, TipoCorrida.PROLABORE, rota)
    
    def valorFinalCorrida(self, rota: Rota) -> None:
        if not rota.distancia:
            raise ValueError("Distancia nao definida")

        valorTotal = rota.distancia * 1.3
        
        self.valorTotal = valorTotal
        
