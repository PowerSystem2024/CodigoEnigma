<script setup>

import { ref } from 'vue';

const experiencias = ref([
    {
        titulo: 'Tecnicatura en Programacion - UTN San Rafael',
        fecha: '2024 - Actual',
        parrafo: 'Incumbencias Profesionales: Operación y programación de computadoras, desarrollo de programas en distintos lenguajes, análisis y control de sistemas informáticos.',
        enlace:'https://www.frsr.utn.edu.ar/programacion/',
        
    },
    {
        titulo: 'Programación y Diseño Web - Escuela Da Vinci',
        fecha: '2019 - 2020',
        parrafo: 'Tecnicatura en Proogramación y Diseño web. Creación de Páginas Web RESS (Responsive + Server Side Components), y Aplicaciones Móviles (Progressive Web Apps).',
        enlace:'https://davinci.edu.ar/carreras/desarrollo-web-y-mobile',
    },
    {
        titulo: 'Traductorado en Inglés - Lenguas Vivas',
        fecha: '2014 - 2016',
        parrafo: 'Especialización en áreas técnicas, científicas y literarias, y con formación en traducción inversa e interpretación.',
        enlace:'https://spangenberg-caba.infd.edu.ar/sitio/traductorado/',
    },
    // Puedes agregar más objetos para cada conjunto de experiencias.
]);
</script>

<template>
    <div class="experiencias">
        <div v-for="experiencia in experiencias" :key="experiencia.titulo" class="card">
            <h3 class="titulo">{{ experiencia.titulo.toLocaleUpperCase() }}</h3>
            <p class="fecha">{{ experiencia.fecha }}</p>
            <p class="parrafo">{{ experiencia.parrafo }}</p>
            <a :href="experiencia.enlace" target="_blank" rel="noopener noreferrer" class="enlace">Más información sobre la carrera</a> 
        </div>
    </div>
</template>

<style scoped>
.experiencias{
    display: flex;
    flex-flow: row nowrap;
    justify-content: start;
    gap:20px;
}
.card {
    
    padding: 1.5rem;
    background-color: #283618;
    border-radius: 15px;
    margin-bottom: 2rem;
    
    width: 33%;
    display: flex;
    flex-flow: column;
    justify-content: space-between;
    

}
.titulo {
    font-size: 1.2rem;
    color: coral;
}

.fecha {
    font-size: 1rem;
    color: burlywood;
    margin-bottom: 1rem;
}

.parrafo{
    margin-bottom: 2em;
}

</style>
