
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon ", 9500.00);
        Producto producto2 = new Producto("Campera ", 29900.00);
        Producto producto3 = new Producto("Zapatillas ", 120000.00);
        Producto producto4 = new Producto("Camisa ", 20000.00);
        Producto producto5 = new Producto("Gorra ", 7000.00);
        Producto producto6 = new Producto("Billetera ", 5500.00);
        Producto producto7 = new Producto("Lentes ", 3000.00);
        Producto producto8 = new Producto("Anillos ", 2500.00);    
        Producto producto9 = new Producto("Medias ", 2000.00);        
        Producto producto10 = new Producto("Pulsea ", 1000.00);
                
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        orden1.agregarProducto(producto6);
        orden1.agregarProducto(producto7);
        orden1.agregarProducto(producto8);
        orden1.agregarProducto(producto9);
        orden1.agregarProducto(producto10);
        orden1.mostrarOrden();
        
        //Tarea:
        //Crear mas objetos de tipo producto = 10
        //Crear mas objetos de tipo orden = 2
        
        System.out.println(); //Separar ordenes
        
        
        Producto producto11 = new Producto("Zapatos", 8500.00);
        Producto producto12 = new Producto("Bufanda", 4500.00);
        Producto producto13 = new Producto("Guantes", 3000.00);
        Producto producto14 = new Producto("Chaqueta", 25000.00);
        Producto producto15 = new Producto("Sombrero", 7500.00);
        Producto producto16 = new Producto("Reloj", 10000.00);
        Producto producto17 = new Producto("Mochila", 15000.00);
        Producto producto18 = new Producto("Collar", 5000.00);
        Producto producto19 = new Producto("Pulsera de cuero", 2000.00);
        Producto producto20 = new Producto("Corbata", 3500.00);
        
        Orden orden2 = new Orden();
        
        orden2.agregarProducto(producto11);
        orden2.agregarProducto(producto12);
        orden2.agregarProducto(producto13);
        orden2.agregarProducto(producto14);
        orden2.agregarProducto(producto15);
        orden2.agregarProducto(producto16);
        orden2.agregarProducto(producto17);
        orden2.agregarProducto(producto18);
        orden2.agregarProducto(producto19);
        orden2.agregarProducto(producto20);
        
       orden2.mostrarOrden();  
    }
}

