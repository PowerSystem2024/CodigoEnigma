//ciclo while 
//si la condicion si es verdadera entra , si es falsa imprime fin del ciclo while
let contador = 0;
while(contador < 3 ){
    console.log(contador);
    contador++;
}
console.log("Fin de ciclo while");

//do while
// aca se ejecuta primero una vez muestra todo osea el 0 y luego revisa la condicion (conteo <3 ) y ahi vuelve a entrar se velve a repetir con el 1 y 2 
// y si no cumple con la condicion es falsa 
let conteo =0;
do{
    console.log(conteo);
    conteo++;
}while(conteo <3);
console.log("Fin de ciclo do while");

//for 
// es lo mismo pero se pone todo en la misma linea ,tambien se pueden definir varias variablkes dentro del mismo
// (c=8 , e=2;) se separa con una , 
// primero se inicializa una variable (let contando = 0;)
// segundo comprobacion , condicion (contando < 3)
//tercero incremento (++) o decremento (--) --> contando++ o contando--
for(let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("fin del ciclo for")

// Palabra reservada break
for(let contando = 0; contando <= 10;contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break; // ROMPE EL CICLO FOR Y SOLO MUESTRA EL PRIMER NUMERO PAR 
    }
}
console.log("Termina el ciclo al encontrar el primer numero par");

// la palabra continue
for(let contando = 0; contando <= 10;contando++){
    if(contando % 2 !== 0){
        continue; // ir a la  siguiente iteracion  
    }
    console.log(contando);
}
console.log("Termina el ciclo");

//Etiquetas labels nos deja ir directamente a alguna parte de nuestro programa
// no son recomendables pero es necesario saberlo 
inicio:
for(let contando = 0; contando <= 10;contando++){
    if(contando % 2 !== 0){
        break inicio; 
    }
    console.log(contando);
}
console.log("Termina el ciclo");