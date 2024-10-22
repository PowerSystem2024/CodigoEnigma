# Clase3
# Ejercicio con Diccionario y tarea

seleccionArgentina = {
    10:{'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo derecho'},
    11:{'Nombre': 'Ángel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo derecho'},
    24:{'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media punta'},
    19:{'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa central'},
    1:{'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
    7:{'Nombre': 'Rodrigo de Paul', 'Edad': 30, 'Altura': 1.80, 'Precio': '30 millones', 'Posicion': 'Centrocampista'},
    24:{'Nombre': 'Enzo Fernandez', 'Edad': 23, 'Altura': 1.78, 'Precio': '75 millones', 'Posicion': 'Centrocampista'},
    5:{'Nombre': 'Leandro Paredes', 'Edad': 30, 'Altura': 1.82, 'Precio': '8 millones', 'Posicion': 'Centrocampista'},
    9:{'Nombre': 'Julian Alvarez', 'Edad': 24, 'Altura': 1.70, 'Precio': '70 millones', 'Posicion': 'Extremo derecho'},
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedó así {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)