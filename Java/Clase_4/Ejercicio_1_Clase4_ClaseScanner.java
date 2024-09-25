//Pedir numeros hasta que se teclee un 0 , mostrar la suma de todos los numeros introducidos
// Clase Scanner
package Clase_4
import java.util.Sacnner;
public class Ejercicio_1_Clase4{
    public static void mqain(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero , suma = 0;
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nexline());
            suma+= numero;
        }while(numero !=0);
        System.out.println("La suma de todos los numeros ingresados es: " +suma);
        
    }
}
