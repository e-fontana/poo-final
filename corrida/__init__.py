from typing import Any, Final
from abc import ABC, abstractmethod

from tipo_corrida import TipoCorrida
from cliente import Cliente

class Corrida(ABC):
    def __init__(self, id: str, cliente, tipo: TipoCorrida) -> None:
        self._id: Final = id
        self._cliente = cliente
        self._tipo = tipo

    def __str__(self) -> str:
        return ""

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Corrida):
            return False
        return (self.getTipo() == value.getTipo()) and (self.getId() == value.getId())
    
    def getId(self) -> str:
        return self._id
    
    def getCliente(self):
        return self._cliente
    
    def getTipo(self) -> TipoCorrida:
        return self._tipo
    
    def setCliente(self, cliente: Cliente):
        self._cliente = cliente

    @abstractmethod
    def valorFinalCorrida(rota):
        pass