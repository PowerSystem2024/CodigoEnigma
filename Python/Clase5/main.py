# Funciones
# mi_funcion # No se puede llamar antes de definirla

def mi_funcion():
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion()

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo
numeroFactorial = int(input('Ingrese un número para calcular el factorial: '))
resultado = factorial(numeroFactorial) # lo hacemos en código duro
print(f'El factorial del número {numeroFactorial} es: {resultado}')