/*Ejercicio 3: Leer numeros hasta que se introduzca un cero para cada uno indicar si es par o impar 
Clase JOptionPane:
 */
//package Clase_3_Ejercicio_con_Ciclos_scanner;

import javax.swing.JOptionPane;

public class Clase_3_Ejercicio_con_Ciclos_JOptionPane {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero != 0){
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El numero ingresado " +numero+  "es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero ingresado " +numero+  "es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado es " +numero+  "finaliza el programa");

    }
}