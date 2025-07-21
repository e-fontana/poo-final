from typing import Any, Final
from abc import ABC, abstractmethod

from tipo_corrida import TipoCorrida
from cliente import Cliente
from endereco.rota import Rota

class Corrida(ABC):
    def __init__(self, id: str, cliente, tipo: TipoCorrida, rota: Rota) -> None:
        self._id: Final = id
        self._cliente = cliente
        self._tipo = tipo
        self._rota: Rota = rota
        self._valorTotal: float | None = None

    def __repr__(self) -> str:
        return f'ID: {self._id}, Nome cliente: {self.cliente.nome}, Tipo: {self.tipo}, Rota: {self.rota}, Valor Total: {self.valor_final_corrida}'

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Corrida):
            return False
        return (self.tipo == value.tipo) and (self.id == value.id)
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def tipo(self) -> TipoCorrida:
        return self._tipo
    
    @property
    def valor_final_corrida(self):
        return self._valorTotal
    
    @property
    def rota(self):
        return self._rota
    
    @rota.setter
    def setRota(self, rota):
        self._rota = rota
    
    @cliente.setter
    def setCliente(self, cliente: Cliente):
        self._cliente = cliente

    @valor_final_corrida.setter
    def set_valor_final_corrida(self, rota: Rota):
        pass

    @abstractmethod
    def calcular_valor_final(self, rota: Rota):
        pass