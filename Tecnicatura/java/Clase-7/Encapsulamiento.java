package java.Clase_7;

public class Encapsulamiento {
    
        //Atributos 
        private String nombre;
        private double sueldo;
        private Boolean eliminado;

        //Constructor
        public Encapsulamiento(String nombre, double sueldo , Boolean _eliminado){
        this.nombre = nombre;//this lo usamos para diferenciar un atributo de una variable , porque son iguales
        this.sueldo = sueldo;// a menos que se le ponga alfo distinto a la variable para diferenciarlo y no hace falta el this 
        eliminado = _eliminado;

    }
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String nombre){
           this.nombre = nombre;
    }
    public double getSueldo(){
        return sueldo;
    }
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }
    public boolean isEliminado(){
        return eliminado;
    }
    public void setEliminado(boolean eliminado){
        this.eliminado = eliminado;
    }

}
