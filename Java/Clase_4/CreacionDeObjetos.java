package Clase_4;
 
 public class CreacionDeObjetos  {
 
    //atributos de la clase
    int a; //cuando a un valor entero lo inicializamos sin ningun valor se le asigna el 0 por default, y en un tipo booleano por default va a salir como false
    int b;
    // metodo
    public void sumarNumeros(){
        //cuerpo de la clase
        int resultado = a + b;
        System.out.println("resultado = "+ resultado);

    }
 }