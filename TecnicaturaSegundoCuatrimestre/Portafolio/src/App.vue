<script setup>
import NavBar from './components/NavBar.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import EducacionComponente from './components/EducacionComponente.vue'
import ExperienciaComponente from './components/ExperienciaComponente.vue'
import ProyectosComponente from './components/ProyectosComponente.vue'
import HabilidadesComponente from './components/HabilidadesComponente.vue'
import InteresesComponente from './components/InteresesComponente.vue'
import FooterComponente from './components/FooterComponente.vue'
</script>

<template>
  <NavBar />

  <main>
    <DatosPersonales />

    <section id="educacion">
      <h2>Educación</h2>
      <EducacionComponente />
    </section>

    <section id="experiencia">
      <h2>Experiencia</h2>
      <ExperienciaComponente />
    </section>

    <section id="proyectos">
      <h2>Proyectos</h2>
      <ProyectosComponente />
    </section>

    <section id="habilidades">
      <h2>Habilidades</h2>
      <HabilidadesComponente />
    </section>

    <section id="intereses">
      <h2>Intereses</h2>
      <InteresesComponente />
    </section>
  </main>

  <FooterComponente />
</template>

<style scoped></style>
