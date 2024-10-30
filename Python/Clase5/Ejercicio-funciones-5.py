# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.
# Investigar las formulas
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia: multiplicación, división y suma

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Ingrese el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F: {resultado:.2f}')

fahrenheit = float(input('Ingrese el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f}')