class Persona:  # Creamos una clase llamada Persona
    # Inicializar objetos mediante el constructor
    def __init__(self, nombre, apellido, edad):  # Método constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Crear una instancia de la clase Persona
persona1 = Persona("Ariel", "Betancud", "40")  # Constructor requiere argumentos

# Imprimir los atributos de persona1
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f"El objeto1 de la clase persona {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")

# Crear otra instancia de la clase Persona
persona2 = Persona("Osvaldo", "Giordanini", "45")
print(f"El objeto2 de la clase persona {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}")

# Se pueden modificar los objetos 
persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = "40"
print(f"El objeto1 de la clase persona {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")

# Los atributos son: características
# Los métodos: el comportamiento que van a tener los objetos (acciones)
