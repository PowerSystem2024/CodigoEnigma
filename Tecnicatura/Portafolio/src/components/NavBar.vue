<script setup>
import { ref } from 'vue'
const navegacion = ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' },
])
</script>

<template>
  <header>
    <p class="logo"><a href="./">&lt;Código Enigma/&gt;</a></p>

    <nav class="navbar">
      <ul>
        <li class="navbar-menu">
          <a
            v-for="nav in navegacion"
            :key="nav.nombre"
            :href="nav.enlace"
            class="nav-item"
            >{{ nav.nombre }}</a
          >
        </li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 6.25rem;
  background-color: var(--black-tertiary);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--white-tertiary);
  position: fixed;  
  top: 0;          
  left: 0;    
  width: 100%; 
  z-index: 1000; 
}

.navbar-item {
  text-decoration: none;
}

.navbar-menu {
  display: flex;
  flex-direction: row;
  gap: 1.25rem;
  justify-content: flex-end;
}

.logo {
  font-family: 'Roboto Mono', serif;
  font-weight: 700;
  color: var(--white-primary);
}

ul {
  list-style: none;
}

li a {
  font-size: 0.875rem;
  text-decoration: none;
  transition: 0.4s;
  padding:  0.625rem;
  align-items: center;
}

li a:hover {
  background-color: var(--hover-color-opacity);
  border-radius: 50px;
  transition: 0.4s;
}

/* Responsive */

@media (max-width: 768px) {
  .navbar-menu {
    display: flex;
    justify-content: flex-end;
    width: 100%;
  }

  .nav-item {
    display: none;
  }
}


</style>
