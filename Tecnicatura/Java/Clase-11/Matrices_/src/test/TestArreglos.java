
package test;

public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int [3]; //el lado izq. declaramos la variable
        //lado derecho instanciamos un objeto de tipo object
        System.out.println("edades = " + edades);
        
        edades [0] = 17;
        System.out.println("edades 0 = " + edades[0]);
        
        edades [1] = 84;
        System.out.println("edades 1 = " + edades[1]);
        
        edades [2] = 56;
        System.out.println("edades 2 = " + edades[2]);
        
        for(int i = 0 ; i < edades.length; i++){
            System.out.println("edades y sus elementos"+i+": "+edades[i]);
        } 
    }
}
