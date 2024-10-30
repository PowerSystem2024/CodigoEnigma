<script setup>
import { ref } from 'vue'
const titulo = 'Desarrollo Full Stack'
const fecha = 'Marzo 2024 | Actualidad'
const experiencias = ref([
  {
    id: 1,
    parrafo:
      'En nuestro proyecto de Java, nuestro equipo desarrolló una aplicación de consola que simula una ruleta de apuestas.',
  },
  {
    id: 2,
    parrafo:
      'La aplicación permite a los usuarios realizar apuestas en diferentes números y colores, y proporciona un sistema de resultados aleatorios que simula el giro de la ruleta.',
  },
])
</script>

<template>
  <div class="card">
    <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
    <p class="fecha">{{ fecha }}</p>
    <ul class="listado">
      <li class="item" v-for="experencia in experiencias" :key="experencia.id">
        <p>{{ experencia.parrafo }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  padding: 2rem;
  background-color: var(--black-secondary);
  border-radius: 15px;
  border: 1px solid var(--white-tertiary);
}

.fecha {
  margin-bottom: 1rem;
}

.listado {
  display: flex;
  flex-direction: column;
}

.item {
  align-items: center;
  display: flex;

  gap: 1.5rem;
}
</style>
