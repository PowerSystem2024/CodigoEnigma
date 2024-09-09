miFuncion(8,2); //esto se lo conoce como hosting podemos declararolo por cualquier lado del codigo si antes de poner la condicion o despues
function miFuncion(a,b){
    //console.log("Sumamos: "+ (a+b));
    return a+b;
}

//llamamos la funcion // me pone los dos resultados 
miFuncion(5,4);

let resultado = miFuncion(6,7);
console.log(resultado);

// Declaramos una funcion de tipo expresion
let x = function(a,b){return a+ b};//necesita cierre con punto y coma
resultado = x(5,6); //al llamarla se pone la variable y parentesis
console.log(resultado);

// Funciones de tipo self y invoking
(function(a, b){
      console.log("Ejecutando la funcion: "+ (a + b));
})(9,6);

//pàra saber cuantos argumentos tiene 
console.log(typeof miFuncion);
function miFuncionDos(a,b){
    console.log(arguments);
}
miFuncionDos(5,7);

//dentro de la funcion funciona
console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}
miFuncionDos(5,7,3,6);

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// Funciones flecha
// es similar con la tipo expresion
const sumarFuncionFlecha = (a, b) => a + b ;
resultado = sumarFuncionFlecha(3, 7);
console.log(resultado);

//Sumar todos los argumentos 
let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta)
function sumarTodo(){
    let suma = 0;
    for(let i = 0;i < arguments.length; i++){
        suma+= arguments[i];
    }
    return suma;
}

//paso por valor y paso por referencia
//paso por valor: es cuando utilizamos tipos que no son objetos ejemplo numericos booleanos etc

//tipos primitivos 
let k = 10 
function cambiarValor(a){// paso por valor no sufre ningun cambio en este caso es la k 
      a=20;
}
cambiarValor(k);
console.log(k) //no cambio el valor porque no se puede cambiar

//paso por referencia: se usa para cambiar los objetos 
// a la funcion le pasamos la referencia exadecimal del espacio de memoria donde esta alojado este objeto
// cuando cremos un objeto se crea un espacio de memoria y al pasarle ese objeto le estamos pasando ese valor exadecimal
//de la memoria y es ahi que dentro de la funcion se modifican esos valores 
const persona = {
    nombre: "Juan",
    apellido: "Lepez"
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = "Ignacio";
    p1.apellido = "Perez";
}

cambiarValorObjeto(persona);
console.log(persona);

