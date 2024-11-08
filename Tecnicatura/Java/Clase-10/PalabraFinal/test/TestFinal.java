/*
Uso de la palabra final
esta palabbra tiene diferentes significados dependiendo donde
se aplique:
        variables: evita cambiar el valor que almacena la variable
        métodos: evita que se modifique la difinición o el comportamiento
                 de un método desde una subclase (hija)
        clases: evita que se creen clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables
se combina con el modifiador de acceso estático para convertir una
variable en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en la cuál todos sus atributos
son un tipo static y final, es por esto que la variable pi* se conoce como una constante
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        //miDni = 203112321; No se puede modificar
        //Persona.CONSTANQUE_AQUI = 9; //No se modifica
         System.out.println("Mi atributo constante es "+Persona.CONSTANQUE_AQUI);
         
         
         final Persona persona1 = new Persona();
         //persona1 = new Persona(); No se puede asignar una nueva referencia
         persona1.setNombre("Ariel Betancud");
         System.out.println("persona1 nombre: "+persona1.getNombre());
         persona1.setNombre("Liliana");
         System.out.println("persona1 nombre: "+persona1.getNombre());
    }
}