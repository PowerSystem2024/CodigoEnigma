package Clase05;


import javax.swing.*;

public class Ciclos04 {
    public static void main(String[] args) {
        System.out.println("Digite el día: ");
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día: "));
        System.out.println("Digite el mes: ");
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        System.out.println("Digite el año: ");
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el año: "));
        if((dia != 0) && (dia <= 31)){
            if((mes != 0) && (mes <= 12)){
                if((anio != 0) && (anio <= 2024)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");        }
    }
}
