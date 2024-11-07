from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '15 Pulgadas')
raton1 = Raton('HP', '15 Pulgadas')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', '27 Pulgadas')
raton2 = Raton('Acer', 'Bluetooth')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)