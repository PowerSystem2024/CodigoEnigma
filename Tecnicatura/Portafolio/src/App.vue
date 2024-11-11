<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import InteresesComponente from './components/InteresesComponente.vue';
</script>

<template>
    <header id="top">
        <!--Barra de Navegacion-->
        <NavBar />
        <!--Componente Datos Personales-->
        <DatosPersonales />
    </header>
    <main>
        <!--el estilo css de section se encuentra en base.css-->
        <section id="educacion">
            <h2>Educación - Cursos</h2>
            <!--Componente Experiencia-->
            <ExperienciaComponente />
        </section>
        <section id="experiencia">
            <h2>Experiencia</h2>
            <!--Componente Educacion-->
            <Educacion />
            
        </section>
        <section id="proyectos">
            <h2>Proyectos</h2>
            <!--Componente Proyectos-->
            <ProyectosComponente />
        </section>
        <section id="habilidades">
            <!--Componente Habilidades-->
            <h2>Habilidades</h2>
            <HabilidadesComponente />
        </section>
        <section id="intereses">
            <!--Componente Intereses-->
            <h2>Intereses</h2>
            <InteresesComponente />
        </section>
    </main>
    <footer>
        <a href="#top">Volver al Inicio</a>
        <p>© 2024 Dilan Ramos - Portafolio web - Estudiante de Programación en la UTN FRSR</p>
    </footer>
</template>

<style scoped>
footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    font-size: 1.3rem;
    font-weight: bold;
    color:#283618;
}
footer a{
    color:#283618;
    border: 1px solid #283618;
    padding: 5px 10px;

}
footer a:hover{
    color:#fefae0;
    background-color: #283618;

}
</style>
