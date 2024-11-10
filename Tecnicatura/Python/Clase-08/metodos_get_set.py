class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre}, {self._apellido}, {self._edad}")

    @property
    def nombre(self):
        print("Estamos utilizando el metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Estamos utilizando el metodo set")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def nombre(self, edad):
        self._edad = edad

if __name__ == '__main__':
    persona1 = Persona2("Prueba", "Clase", 8)
    persona1.mostrar_detalles()
    print(persona1.nombre)
    persona1.nombre = "Juan Pedro"
    print(persona1.nombre)
    print(persona1.mostrar_detalles())