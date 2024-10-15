<script setup>
import { ref } from 'vue'
const navegacion = ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
])
</script>

<template>
  <header>
    <nav class="navbar">
      <ul class="navbar-menu">
        <li><a href="#educacion" class="navbar-item">Educación</a></li>
        <li><a href="#experiencia" class="navbar-item">Experiencia</a></li>
        <li><a href="#proyectos" class="navbar-item">Proyectos</a></li>
        <li><a href="#habilidades" class="navbar-item">Habilidades</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="educacion">
      <h2>Educación - Cursos</h2>
    </section>
    <section id="experiencia">
      <h2>Experiencia</h2>
    </section>
    <section id="proyectos">
      <h2>Proyectos</h2>
    </section>
    <section id="habilidades">
      <h2>Habilidades</h2>
    </section>
    <section id="intereses">
      <h2>Intereses</h2>
    </section>
  </main>
</template>

<style scoped>
.navbar {
  color: #fff;
  padding: 0.5rem 1rem;
  align-items: center;
}

.navbar-item {
  color: #fff;
  text-decoration: none;
  margin-right: 1rem;
}

.navbar-menu {
  display: flex;
  justify-content: flex-end;
}

.nav-list {
  list-style: none;
}

a {
  text-decoration: none;
  transition: 0.4s;
  padding: 10px;
}

a:hover {
  background-color: #ffffff11;
  border-radius: 5px;
  transition: 0.4s;
}

@media (max-width: 768px) {
  .navbar-menu {
    display: flex;
    justify-content: flex-end;
    width: 100%;
  }
}
</style>
