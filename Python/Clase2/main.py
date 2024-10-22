# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # función len = length

# Revisar si un elemento existe dentro de set
print('marte' in planetas)

# Agregar un elemento
planetas.add('Tierra') # Add es una función

# Eliminar elemento, arroja error si no existe
planetas.remove('Júpiter')
print(planetas)
planetas.discard('tierra') # Esta función no nos presenta error

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas

# Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Bases de Datos'
}
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos un elemento
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'

# Cómo recorrer los elementos
for termino in diccionario:
    print (termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values():
    print(valor) # Muestra solo los valores

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario