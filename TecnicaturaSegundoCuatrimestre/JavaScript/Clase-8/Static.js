class Persona{ 

    static contadorPersona = 0; // Atributo estatico
    // email = 'Valor default email'; // Atributo no estatico

    static get MAX_OBJ(){
        return 5;
    }

    constructor(nombre, apellido) { 
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersona < Persona.MAX_OBJ){
            this.idPersona = ++ Persona.contadorPersona;
        }else{
            console.log('Se ha superado el maximo de objetos permitidos');
        }
        
        /*
        * Incremento del contador: Cada vez que se crea una nueva instancia de Persona, dentro del constructor, se incrementa el valor de 
        contadorObjetosPersona usando Persona.contadorObjetosPersona++. Esto lleva un control de cuántas instancias de Persona se han 
        creado.
        * contadorObjetosPersona es una propiedad estática que lleva la cuenta de cuántos objetos de la clase Persona o Empleado se han 
        creado.
        * Los métodos estáticos son llamados desde la clase, no desde las instancias.
        */
        //console.log('Se incrementa el contador: ' + Persona.contadorObjetosPersona)
    }

    // Método getter para obtener el nombre
    get nombre() {
        return this._nombre; // Devuelve el valor del atributo _nombre
    }

    // Método getter para obtener el apellido
    get apellido() {
        return this._apellido; // Devuelve el valor del atributo _apellido
    }

    // Método setter para establecer un nuevo nombre
    set nombre(nombre) { 
        this._nombre = nombre; // Asigna un nuevo valor al atributo _nombre
    }

    // Método setter para establecer un nuevo apellido
    set apellido(apellido) {
        this._apellido = apellido; // Asigna un nuevo valor al atributo _apellido
    }

    nombreCompleto(){
        return this.idPersona + ' ' + this._nombre + " " + this._apellido;
    }
    // Sobreescribimos el metodo de la clase padre (Object)
    toString(){ 
        return this.nombreCompleto();
    }

    // Static
    static saludar(){
        console.log('Saludos desde este metodo static');
    }

    static saludar2(persona){
        console.log(persona.nombre + ' ' + persona.apellido);
    }
}

class Empleado extends Persona { // Clase hija que hereda de Persona
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido); // Llama al constructor de la clase padre (Persona) para inicializar _nombre y _apellido
        this._departamento = departamento; // Inicializa el atributo privado _departamento
    }

    // Método getter para obtener el departamento
    get departamento() {
        return this._departamento; // Devuelve el valor del atributo _departamento
    }

    // Método setter para establecer un nuevo departamento
    set departamento(departamento) {
        this._departamento = departamento; // Asigna un nuevo valor al atributo _departamento
    }

    // Sobreescritura: modificar el comportamiento de algun metodo definido en la clase padre
    nombreCompleto(){
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

let persona1 = new Persona('Martin', 'Perez');
persona1.nombre = 'Juan Carlos';
console.log(persona1)

// Object.prototype.toString Esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

// Los metodos estaticos se asocian con una clase pero no con un objeto, no se utiliza desde el objeto
//persona1.saludar(); // persona1.saludar is not a function
Persona.saludar()
Persona.saludar2(persona1)
// Estos solo se van a mostrar desde la consola

// Heredamos el metodo estatico a la clase hija
Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
// Desde la clase hija lo llamamos
console.log(Empleado.contadorObjetosPersona);

// Atributo estatico se asocia a la clase en si 
// Atributo estatico se asocia solo a los objetos
console.log(persona1.email);
// Accediendo al objeto de la clase hija
console.log(empleado1.email);
// console.log(Persona.email); // No es estatico, no se puede acceder desde la clase en si
console.log(empleado1.toString())
console.log(persona1.toString())
console.log(Persona.contadorPersona)

let persona3 = new Persona('Carla', 'Pertosi')
console.log(persona3.toString())
console.log(Persona.contadorPersona)

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; // No se puede modificar, ni alterar

let persona4 = new Persona('Franco', 'Diaz')
console.log(persona4.toString())
let persona5 = new Persona('Ariel', 'Betancud')
console.log(persona5.toString())
let persona6 = new Persona('Liliana', 'Paz')
console.log(persona6.toString())