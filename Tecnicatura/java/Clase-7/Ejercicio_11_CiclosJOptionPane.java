/*
 * Ejercicio 11 : Diseñar un programa que muestre el producto de los primeros numeros impares hacerlo con JOptionPane
 */

package java.Clase_7;

import javax.swing.JOptionPane;

public class Ejercicio_11_CiclosJOptionPane {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i<=20; i+=2){
            producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los numeros impares es: " +producto);
    }
}
