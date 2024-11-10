from Cuadrado import Cuadrado
from Rectanculo import Rectangulo

cuadrado1 = Cuadrado(5,  "Azul")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Calculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(3, 8, "Verde")
print(f"Calculo del area del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)