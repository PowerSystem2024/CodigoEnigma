let x = 10
console.log(x.length)
console.log('Tipos primitivos')

let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    idioma: 'es',
    get lang() {
        return this.idioma.toUpperCase()
    },
    set lang(lang) {
        this.idioma = lang.toUpperCase()
    },
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido
    },
    get nombreEdad() {
        return 'El nombre es: ' + this.nombre + ', Edad: ' + this.edad
    }
}

console.log(persona.nombre)
console.log(persona.apellido)
console.log(persona.email)
console.log(persona.edad)
console.log(persona)

console.log(persona.nombreCompleto())

console.log('Ejecutando con un objeto:')
let persona2 = new Object()
persona2.nombre = 'Juan'
persona2.direccion = 'Saturno 15'
persona2.telefono = '55443322'

console.log(persona2.telefono)

console.log('Creamos un nuevo objeto: ')
console.log(persona['apellido'])

console.log('Usamos el ciclo for in: ')
for (propiedad in persona) {
    console.log(propiedad)
    console.log(persona[propiedad])
}

console.log('Cambiamos y eliminamos un error: ')
persona.apellido = 'Perez'
delete persona.apellido
console.log(persona)

console.log('Distintas formas de imprimir un objeto: Forma 1 ')
console.log(persona.nombre + ' ' + persona.apellido)

console.log('Distintas formas de imprimir un objeto: Forma 2 ')
for (nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad])
}

console.log('Distintas formas de imprimir un objeto: Forma 3 ')
let personaArray = Object.values(persona)
console.log(personaArray)

console.log('Distintas formas de imprimir un objeto: Forma 4 ')
let personaString = JSON.stringify(persona)
console.log(personaString)

console.log('Comenzamos a utilizar el método get: ')
console.log(persona.nombreEdad)

console.log('Comenzamos con el método get para idiomas: ')
persona.lang = 'en'
console.log(persona.lang)

function Persona3 (nombre, apellido, email) {
    this.nombre = nombre
    this.apellido = apellido
    this.email = email
    this.nombreCompleto = function() {
        return this.nombre + ' ' + this.apellido
    }
}

let padre = new Persona3('Juan', 'Perez', 'juanperez@gmail.com')
padre.nombre = 'Leo'
padre.telefono = '55443322'
console.log(padre)
console.log(padre.nombreCompleto())

let madre = new Persona3('Laura', 'Quintero', 'laura@gmail.com')
console.log(madre)
console.log(madre.telefono)
console.log(madre.nombreCompleto())

// Formas de crear un objeto
let miObjeto = new Object()

let miObjeto2 = {}

let miCadena1 = new String('Hola')

let miCadena2 = 'Hola'

let miNumero = new Number(1)

let miNumero2 = 1

let miBoolean = new Boolean(false)

let miBoolean2 = false

let miArreglo = new Array()

let miArreglo2 = []

let miFuncion = new Function()

let miFuncion2 = function() {}

// Uso de prototype
Persona3.prototype.tel = '55443322'
console.log(padre)
console.log(madre.telefono)
madre.telefono = '011581032'
console.log(madre.telefono)

// Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto: function(titulo, telefono) {
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ' ' + telefono
        // return this.nombre+''+this.apellido
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic', '55443322'))
console.log(persona4.nombreCompleto2.call(persona5, 'Ing', '011581032'))

let arreglo = ['Ing', '011581032']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo))