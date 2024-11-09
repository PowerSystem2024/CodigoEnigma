/*
Ejercicio 1: Leer 10 números enteros, guardarlos en un arreglo. Debemos mostrarlos
en el siguiente orden: el primero, el último, el segundo, el penúltimo,
el tercero, etc.
*/
package ejercicio_1_laboratorio;

import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int[10];
        
        for (int i=0; i<10; i++) {
            System.out.print((i+1)+". Digite un numero: ");
            numeros [i] = entrada.nextInt();
        }
        System.out.print("El resultado es: ");
        for (int i=0; i<5;i++) {
            System.out.print(numeros[i]+" "); //Primero, segundo
            System.out.print(numeros[9-i]+" "); //ultimo, penultimo
        }
        System.out.println(); //Salto de linea
    }
    
}
