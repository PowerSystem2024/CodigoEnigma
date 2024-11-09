/*
 * Ejercicio 12: Pedir un numero y calcular
 * su factorial hacerlo con la clase scanner y JOptionPane
 */

package java.Clase_6_Caja;

import javax.swing.JOptionPane;

public class Ejercicio12ClaseScannerYJOptionPane {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial =1;
        //System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for(int i=1; i<=numero ; i++);{
              factorial *= i ;
     }
      //System.out.pritnln("EL factorial del numero ingresado es: "+factorial);
      JOptionPane.showMessageDialog(null, "EL factorial del numero ingresado es: "+factorial);
    }
}


