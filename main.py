from ufber import Ufber
from corrida.entrega import Entrega
from corrida.prolabore import Prolabore
from corrida.carona import Carona
from cliente import Cliente
from endereco.endereco import Endereco
from endereco.rota import Rota

ufber = Ufber()

cliente1 = Cliente('joao kishimoto', '(71) 90000-0000', '000.000.000-00')
cliente2 = Cliente('eduardo fontana', '(71) 90000-0000', '000.000.000-00')

ufba_canela = Endereco('ufba-canela', 'rua do canela', '11', 'canela')
ufba_federacao = Endereco('ufba-federacao', 'rua da federacao', '02', 'Federacao')
ufba_ondina = Endereco('ufba-ondina', 'rua das gordinhas', '02', 'Ondina')

rota1 = Rota(ufba_canela, ufba_ondina)
rota2 = Rota(ufba_ondina, ufba_federacao)
rota3 = Rota(ufba_federacao, ufba_canela)
rota4 = Rota(ufba_federacao, ufba_ondina)

rota1.set_distancia = 1
rota2.set_distancia = 2
rota3.set_distancia = 3
rota4.set_distancia = 4

prolabore = Prolabore("123", cliente1, rota1)
carona = Carona("12", cliente2, rota2, 0.5)
entrega = Entrega("3", cliente1, rota3)

ufber.add_corrida(prolabore)
ufber.add_corrida(carona)
ufber.add_corrida(entrega)

print(f"Comparação verdadeira: {prolabore == prolabore}")
print(f"Comparação falsa: {prolabore == entrega}")

print(prolabore)
print(ufber.resumo_corridas())