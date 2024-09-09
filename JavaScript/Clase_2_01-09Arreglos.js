//Creaccion de Array o Arreglos
//let autos = new Array("Ferarrari", "Renault", "BMW"); Esta es la sintaxis vieja 
const autos = ["Ferarrari", "Renault", "BMW"];
console.log(autos);

//Recorremos los elementos de un arreglo
//manual
console.log(autos[0]);
console.log(autos[2]);
// con el ciclo for
for(let i = 0; i < autos.length; i++){
    console.log(i+" : " +autos[i]);
}
// Modificamos los elementos del arreglo
autos[1] = "Volvo";
console.log(autos[1]);

//agregar nuevos valores al arragelo
autos.push("Audi"); //agregamos el elemento al final del arreglo
console.log(autos);

// Otras formas de agregar elementos al arreglo
autos[autos.length] = "Porche";
console.log(autos);

//OTRA FORMA DE AGREGAR ELEMENTOS AL ARREGLO TENIENDO CUIDADO
autos[6] = "Renault"; //porque si ponemos m,as los numeros quedan espacios vacios y ocupan memorial al pepe
console.log(autos);

// Como preguntar si es un Array o un Arreglo
console.log(Array.isArray(autos)); // Devuelve un elemento booleano

// Otra forma de preguntar si es Array o Arreglo
console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array