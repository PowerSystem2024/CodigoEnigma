class Vehiculo:
#Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto
#y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase padre debe
##tener los siguientes atributos y métodos

    #Vehiculo (Clase padre)
    #-Atributos(color ruedas)
    #-Métodos(__init__(color, ruedas) y __str__())

    #Auto(clase hija de vehiculo)
    #-Atributos(velocidad (hm/hr)
    #-Métodos(__init__(color, ruedas, velocidad) y __srt__())

    #Bicicleta(clase hija de vehiculo)
    #-Atributos(tipo(urbana/montaña.etc-)
    #-Métodos(__init__(color, ruedad, tipo) y __str__()

    ##Crear un objeto de cada clase

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: "+self.color+", Ruedas: "+str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__() + ", Velocidad(Km/hr): " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+", Tipo: "+self.tipo

vehiculo = Vehiculo("Gris ", 4)
print(vehiculo)

auto = Auto("Rojo ", 4, 128)
print(auto)
bici = Bicicleta("Negro ", 2, "Urbana")

