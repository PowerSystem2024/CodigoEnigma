<script setup>
import { ref } from 'vue'

const fechaColor = ref([])
fechaColor.value = [{ color: '#e0eafe53' }, { color: '#e0eafe53' }]

const educacion = ref([
  {
    fecha: '2024',
    title: 'Tecnicatura Universitaria en Programación',
    descripcion:
      'Incumbencias Profesionales: Operación y programación de computadoras, desarrollo de programas en distintos lenguajes, análisis y control de sistemas informáticos.',
    sitio: 'Universidad Tecnológica Nacional',
  },
  {
    fecha: '2023',
    title: 'Full Stack Developer',
    descripcion:
      'Desarrollo y mantenimiento de aplicaciones web, tanto en el frontend como en el backend, manejo de bases de datos, integración de APIs e implementación de sistemas de control de versiones.',
      sitio: 'Platzi',
  },
])
</script>

<template>
  <ul>
    <li
      v-for="(item, index) in educacion"
      :key="index"
      :style="{ '--fecha-color': fechaColor[index].color }"
    >
      <p class="fecha">{{ item.fecha }}</p>
      <h3 class="title">{{ item.title }}</h3>
      <p class="sitio">{{ item.sitio }}</p>
      <p class="descripcion">{{ item.descripcion }}</p>
    </li>
  </ul>
</template>

<style scoped>
ul {
  margin-top: 2rem;
  --col-gap: 2rem;
  --row-gap: 2rem;
  --line-w: 0.25rem;
  display: grid;
  grid-template-columns: var(--line-w) 1fr;
  grid-auto-columns: max-content;
  column-gap: var(--col-gap);
  list-style: none;

  margin-inline: auto;
}

ul::before {
  content: '';
  grid-column: 1;
  grid-row: 1 / span 20;
  background: rgb(225, 225, 225);
  border-radius: calc(var(--line-w) / 2);
}

ul li:not(:last-child) {
  margin-bottom: var(--row-gap);
}

ul li {
  grid-column: 2;
  --inlineP: 1.5rem;
  margin-inline: var(--inlineP);
  grid-row: span 2;
  display: grid;
  grid-template-rows: min-content min-content min-content;
}

ul li .fecha {
  --dateH: 3rem;
  height: var(--dateH);
  margin-inline: calc(var(--inlineP) * -1);
  text-align: center;
  background-color: var(--fecha-color);
  color: white;
  font-size: 1.25rem;
  font-weight: 700;
  display: grid;
  place-content: center;
  position: relative;
  border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2);
}

ul li .fecha::before {
  content: '';
  width: var(--inlineP);
  aspect-ratio: 1;
  background: var(--fecha-color);
  background-image: linear-gradient(rgba(0, 0, 0, 0.2) 100%, transparent);
  position: absolute;
  top: 100%;
  clip-path: polygon(0 0, 100% 0, 0 100%);
  right: 0;
}

ul li .fecha::after {
  content: '';
  position: absolute;
  width: 1rem;
  aspect-ratio: 1;
  background: var(--bgColor);
  border: 0.3rem solid var(--fecha-color);
  border-radius: 50%;
  top: 50%;
  transform: translate(50%, -50%);
  right: calc(100% + var(--col-gap) + var(--line-w) / 2);
}

ul li .sitio {
  font-weight: 600;
}

ul li .title,
ul li .descripcion,
ul li .sitio {
  background: var(--bgColor);
  position: relative;
  padding-inline: 1.5rem;
}

ul li .title {
  overflow: hidden;
  padding-block-start: 1.5rem;
  padding-block-end: 1rem;
  font-weight: 700;
}

ul li .descripcion {
  padding-block-end: 1.5rem;
  font-weight: 300;
}

ul li .title::before,
ul li .descripcion::before {
  content: '';
  position: absolute;
  width: 90%;
  height: 0.5rem;
  left: 50%;
  border-radius: 50%;
  filter: blur(4px);
  transform: translate(-50%, 50%);
}

ul li .title::before {
  bottom: calc(100% + 0.125rem);
}

ul li .descripcion::before {
  z-index: -1;
  bottom: 0.25rem;
}

@media (min-width: 40rem) {
  ul {
    grid-template-columns: 1fr var(--line-w) 1fr;
  }
  ul::before {
    grid-column: 2;
  }
  ul li:nth-child(odd) {
    grid-column: 1; /* Coloca los ítems impares en la primera columna */
  }
  ul li:nth-child(even) {
    grid-column: 3; /* Coloca los ítems pares en la tercera columna */
  }

  /* Ajuste para que el segundo ítem abarque dos filas */
  ul li:nth-child(2) {
    grid-row: 2/4; /* El segundo ítem ocupará desde la segunda hasta la cuarta fila */
  }

  /* Ajustes específicos para los ítems impares */
  ul li:nth-child(odd) .fecha::before {
    clip-path: polygon(
      0 0,
      100% 0,
      100% 100%
    ); /* Invierte el triángulo en los ítems impares */
    left: 0; /* Alinea el triángulo a la izquierda */
  }

  ul li:nth-child(odd) .fecha::after {
    transform: translate(
      -50%,
      -50%
    ); /* Ajusta la posición del círculo en los ítems impares */
    left: calc(
      100% + var(--col-gap) + var(--line-w) / 2
    ); /* Coloca el círculo a la derecha de la línea */
  }

  ul li:nth-child(odd) .fecha {
    border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0; /* Ajusta los bordes redondeados para los ítems impares */
  }
}

/* Estilo para los créditos */
.credits {
  margin-top: 1rem; /* Espaciado superior para los créditos */
  text-align: right; /* Alinea el texto de los créditos a la derecha */
}
.credits a {
  color: var(--color); /* Aplica el color de texto definido en la variable */
}
</style>
