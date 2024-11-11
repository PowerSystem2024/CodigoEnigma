<script setup>
import linkedin from '/src/assets/linkedin_icon.svg';
import github from '/src/assets/github_icon.svg';
import cv from '/src/assets/cv_resume_icon.svg';


const title = 'Dilan Ramos';
const descripcion = 'Alumno de la Tecnicatura en Programación - UTN';
const residencia = 'San Rafael, Mendoza, Argentina';
const presentacion = 'Desarrollador web Front-End con cinco años de experiencia en el rubro IT y Marketing Digital. Especialización en desarrollo con CMS y tecnologías que incluyen WordPress, WooCommerce, Shopify, headless CMS, HTML, CSS y JavaScript. Experto en troubleshooting y mejorar la experiencia del usuario y SEO.';
const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin, url: 'https://www.linkedin.com/in/dilanramos' },
  { id: 2, name: 'github', src: github, url: 'https://github.com/dilancio' },
  { id: 3, name: 'curriculum', src: cv, url: '/src/assets/CV-Español.pdf' },
];
const telefono = '+54 9 1134149330';
</script>

<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
        </li>
      </ul>
      <h3>☎ {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>


h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color:#fefae0;
}

.card {
  background-color: #606c38;
  border-radius: 10px;
  padding: 40px;
  text-align: center;
 

}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(28, 41, 52);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}

</style>