<script setup>
import { ref } from 'vue'

const habilidades = ref([
  {
    id: 1,
    nombre: 'Lenguajes de Programación',
    habilidades: [
      { id: 1, nombre: 'JavaScript' },
      { id: 2, nombre: 'Python' },
      { id: 3, nombre: 'HTML/CSS' },
      { id: 4, nombre: 'Java' },
      { id: 5, nombre: 'SQL' },
    ],
  },
  {
    id: 2,
    nombre: 'Frameworks y Librerías',
    habilidades: [
      { id: 1, nombre: 'Vue.js' },
      { id: 2, nombre: 'React.js' },
      { id: 3, nombre: 'Node.js' },
      { id: 4, nombre: 'Django' },
      { id: 5, nombre: 'Bootstrap' },
    ],
  },
  {
    id: 3,
    nombre: 'Herramientas de Desarrollo',
    habilidades: [
      { id: 1, nombre: 'Git' },
      { id: 2, nombre: 'GitHub' },
      { id: 3, nombre: 'Visual Studio Code' },
      { id: 4, nombre: 'Postman' },
      { id: 5, nombre: 'Docker' },
    ],
  },
])
</script>

<template>
  <div class="habilidades">
    <ul class="habilidades-lista">
      <li
        class="habilidad"
        v-for="habilidad in habilidades"
        :key="habilidad.id"
      >
        <h3>{{ habilidad.nombre }}</h3>
        <p>{{ habilidad.habilidades.map(item => item.nombre).join(' - ') }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.habilidades {
  width: 100%;
  margin-top: 2rem;
}

.habilidades-lista {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.habilidad {
  width: 100%;
  padding: 1rem;
  border: 1px solid var(--white-tertiary);
  border-radius: 8px;
  background-color: var(--black-secondary);
}

ul li {
  list-style: none;
}
</style>
