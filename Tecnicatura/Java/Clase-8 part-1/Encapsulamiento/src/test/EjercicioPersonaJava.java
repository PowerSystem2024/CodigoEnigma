//Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
//y imprimir, luego modificar sus valores y volver a imprimir
package test;

import dominio.Persona;

public class EjercicioPersonaJava {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan Cruz", 23.500, true);
        System.out.println("persona1 con su nombre es: "+persona1.getNombre());
        System.out.println("persona1 con su sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 con su booleano es: "+persona1.isEliminado());
        persona1.setNombre("Ignacio");
        persona1.setSueldo(50.000);
        persona1.setEliminado(false);
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo modificado : "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano modificado : "+persona1.isEliminado());
    }
}
