/*
Ejercicio 6: Leer dos series de 10 enteros, que estarán ordenados crecientemente.
Copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenadas.
 */
package ejercicio_6;

import java.util.Scanner;

public class Ejercicio_6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int a[] = new int [10];
        int b[] = new int [10];
        int c[] = new int [20];
        boolean creciente = true;
        
        System.out.println("Llenar el primer arreglo: ");
        do{
            for(int i=0;i<10;i++){
                System.out.print((i+1)+". Digite un numero: ");
                a[i] = entrada.nextInt();
            }
            //Comprobamos si el arreglo esta ordenado
            for(int i=0; i<9;i++){
                if(a[i] < a[i+1]){ //Creciente 1-2-3
                    creciente = true;
                }
                //Decreciente 3-2-1
                if (a[i] > a[i+1]){
                    creciente = false;
                    break;
                } 
            }
            if(creciente == false){
                System.out.println("\nEl arreglo esta desordenado, vuelva a digitar: ");
            }
        } while(creciente == false);
        
        System.out.println("Llenar el segundo arreglo: ");
        do{
            for(int i=0;i<10;i++){
                System.out.print((i+1)+". Digite un numero: ");
                b[i] = entrada.nextInt();
            }
            for(int i=0; i<9;i++){
                if(b[i] < b[i+1]){ 
                    creciente = true;
                }
                if (b[i] > b[i+1]){
                    creciente = false;
                    break;
                } 
            }
            if(creciente == false){
                System.out.println("\nEl arreglo esta desordenado, vuelva a digitar: ");
            }
        } while(creciente == false);
        
        int i=0; //Iterador i para el arreglo a
        int j=0; //Iterador j para el arreglo b
        int k=0; //Iterador k para el arreglo c
        
        while(i<10 && j<10){
            if(a[i]< b[j]){ //Si el elemento de a es menor de b
                c[k] = a[i]; //Copiamos el elemento de a
                i++; //Avanzamos una posicion en a
            }
            else {
                c[k] = b[j]; //Copiamos el elemento de b
                j++; //Avanzamos una posicion mas en b
            }
            k++;//Avanzamos una posicion mas en c
        }
        //Cuando salimos del while es porque el arreglo(a o b) se a copiado completamente
        if(i==10){ //Significa que ya copiamos todo el arreglo a, falta el b
            while(j<10) { //Mientras el iterado sea menor a 10
                c[k] = b[j]; //Copiamos el elemento de b en c
                j++; //Avanzamos una posicion en b
                k++; //Avanzamos una posicion en c
            }
        }
        else {
                while(i<10){
                    c[k] = a[i];
                    i++;
                    k++;
                }
        }
        System.out.println("\nEl arreglo c completo es: ");
        for(k=0;k<20;k++){
            System.out.print(c[k]+" - ");
        }
        System.out.println();
    }
}
