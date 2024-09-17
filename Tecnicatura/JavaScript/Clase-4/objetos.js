let x = 10
console.log(x.length)
console.log('Tipos primitivos')

let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido
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