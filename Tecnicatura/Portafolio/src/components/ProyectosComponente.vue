<script setup>
import proyecto1 from '../assets/image.png'
import proyecto2 from '../assets/image.png'

import { ref } from 'vue'
var misProyectos = ref([])

misProyectos.value = [
  {
    id: 1,
    src: proyecto1,
    titulo: 'Aplicación de Reservas para Restaurantes (2023)',
    descripcion:
      'Creé una aplicación móvil con Flutter que permite a los usuarios reservar mesas en restaurantes locales',
    projectoLink: 'https://www.google.com.ar',
    githubLink: 'https://github.com/usuario/proyecto',
  },
  {
    id: 2,
    src: proyecto2,
    titulo: 'Plataforma de E-learning (2022)',
    descripcion:
      'Diseñé y desarrollé una plataforma de educación en línea utilizando Django y React. Con diferentes funcionalidades',
    projectoLink: 'https://www.google.com.ar',
    githubLink: 'https://github.com/usuario/proyecto',
  },
]
</script>

<template>
  <div class="galeria">
    <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
      <img :src="proyecto.src" :alt="proyecto.titlulo" />
      <div class="proyecto-info">
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.descripcion }}</p>
        <div class="proyecto-links">
          <a
            :href="proyecto.projectoLink"
            class="btn-ver-mas"
            target="_blank"
            rel="noopener noreferrer"
            >Ver Proyecto</a
          >
          <a
            :href="proyecto.githubLink"
            class="github-link"
            target="_blank"
            rel="noopener noreferrer"
            >Ver Código en GitHub</a
          >
        </div>
      </div>
    </li>
  </div>
</template>

<style scoped>
.galeria {
  width: 100%;
  height: 100%;
  display: flex;
  gap: 20px;
  justify-content: center;
  text-align: center;
}

.proyecto {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--white-tertiary);
  border-radius: 8px;
  overflow: hidden;
  background-color: var(--black-secondary);
  text-align: center;
}

.proyecto img {
  width: 100%;
  height: auto;
  display: block;
}

.proyecto-info {
  padding: 15px;
  text-align: center;
}

.proyecto-info h3 {
  margin: 10px 0;
  font-size: 1.3em;
  text-align: center;
}

.proyecto-info p {
  margin: 10px 0;
  font-size: 1em;
}

.proyecto-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-top: 3rem;
}

.proyecto-links .btn-ver-mas {
  border: 1px solid var(--white-secondary);
  padding: 10px 15px;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s;
}

.proyecto-links .btn-ver-mas:hover {
  background-color: var(--hover-color-opacity);
}

.proyecto-links .github-link {
  text-decoration: none;
  font-size: 0.9em;
}

.proyecto-links .github-link:hover {
  text-decoration: underline;
}

a {
 align-items: center;
}
</style>
