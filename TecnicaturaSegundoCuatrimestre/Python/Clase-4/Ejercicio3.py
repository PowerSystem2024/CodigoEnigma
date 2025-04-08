# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca en número 0, nuestro proframa dejaría de insertar
# Por último, mostrar los números ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Ingrese un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # lista ordenada
print(f'\nLista ordenada: \n{lista}')