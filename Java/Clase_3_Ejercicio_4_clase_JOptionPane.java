//Ejercicio Nº4: Pedir numeros hasta que se teclee uno negativo , y mostrar cuantos numeros se han introducido.
//Clase JOptionPane

import javax.swing.JOptionPane;

public class Clase_3_Ejercicio_4_clase_JOptionPane {
    public static void main(String[] args) {
    int numero, conteo = 0;
    numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
    while (numero >= 0){
        JOptionPane.showMessageDialog(null,"El numero "+numero+ "es POSITIVO");
        conteo++;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
            
        }
    JOptionPane.showMessageDialog(null,"A ingresado "+conteo+" numeros que no son negativos ");
}
}