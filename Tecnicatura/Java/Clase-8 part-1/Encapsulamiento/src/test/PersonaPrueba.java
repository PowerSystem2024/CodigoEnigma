
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 con su nombre es: "+persona1.getNombre());
        //Modificar a través de los m+etodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("persona1 = " + persona1);
    }
}
