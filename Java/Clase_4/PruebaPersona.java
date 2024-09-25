package Clase_4;
public class PruebaPersona{
    public static void main(String[] args) {
        persona persona1;
        persona1 = new persona(); //llamamos al constructor
        persona1.nombre = "Ariel"; //El valor hexadecimal normalmente comienza en 0x
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion();

        persona persona2 = new persona();
        System.out.println("persona2 = " +persona2); //nos debe imprimir Clases.persona y la direccion de memoria de donde esta alojado 
        System.out.println("persona1 = " +persona1); //nos debe imprimir Clase_4.persona y la direccion de memoria de donde esta alojado
        persona2.obtenerInformacion();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }
}

