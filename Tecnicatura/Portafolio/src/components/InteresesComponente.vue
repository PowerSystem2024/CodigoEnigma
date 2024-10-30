<script setup>
import { ref } from 'vue'

const intereses = ref([
  'Desarrollo de Software de Código Abierto: Contribuyo a proyectos en GitHub, colaborando con otros desarrolladores para mejorar herramientas y librerías populares.',
  'Deportes al Aire Libre: Disfruto del senderismo y el ciclismo de montaña, actividades que practico regularmente para mantener un equilibrio entre el trabajo y la vida personal.',
  'Tecnología de Innovación: Me apasiona explorar nuevas tendencias tecnológicas como la inteligencia artificial y el desarrollo de aplicaciones móviles.',
  'Fotografía: Practico la fotografía como un hobby, lo que me ayuda a mantener una perspectiva creativa tanto en mi vida profesional como personal.',
])
</script>

<template>
  <div class="intereses-contenedor">
    <FondoLava />
    <ul class="contenedor-lista">
      <li class="item" v-for="interes in intereses" :key="interes">
        {{ interes }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor {
  width: 100%;
  margin-top: 2rem;
  padding: 2rem 0;
  position: relative;
}

.contenedor-lista {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  padding: 0;
  margin: 0;
}

.item {
  width: 100%;
  padding: 1rem;
  border: 1px solid var(--white-tertiary);
  border-radius: 8px;
  background-color: var(--black-secondary);
  color: var(--white-primary);
}

.item:nth-child(odd) {
  background-color: var(--black-primary);
}

.item:nth-child(even) {
  background-color: var(--black-secondary);
}

ul li {
  list-style: none;
}
</style>
