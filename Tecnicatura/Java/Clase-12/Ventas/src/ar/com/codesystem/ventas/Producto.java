
package ar.com.codesystem.ventas;

public class Producto {
   //Atributos de la lase
   private int idProducto;
   private String nombre;
   private double precio;
   private static int contadorProductos;

   //Constructor vacio
   private Producto(){
	this.idProducto = ++Producto.contadorProductos;
    }

   public Producto(String nombre, double precio){
	this(); //Llamamos al constructor vacio para el aumento del idProducto
	this.nombre = nombre;
	this.precio = precio;
    }

   public int getIdProducto() {
	return this.idProducto;
    }

   public void setIdProducto(int idProducto) {
	this.idProducto = idProducto;

    }


   public String getNombre()  {
	return this.nombre;
    }


   public void setNombre(String nombre) {
	this.nombre = nombre;
    }


   public double getPrecio() {
	return precio;
    }


   public void setPrecio(double precio) {
	this.precio = precio;
    }
  
   
   @Override
   public String toString(){
       return "Producto{" + "idProducto=" + idProducto + ", nombre=" + nombre + ", precio= " + precio + "}";
   }
}























