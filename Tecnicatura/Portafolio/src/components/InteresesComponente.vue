<script setup>
import { ref } from 'vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
    'Naturaleza',
    'Cuidado ambiental',
    'Cocina',
    'Deporte',
    'Meditación',
    'Lectura',
    'Viajar'
]);
</script>

<template>
    <div class="intereses-contenedor">
        
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
    <!-- <div class="intereses-contenedor">
        <ul class="contenedor-lista">
            <li class="item">
                Desarrollo de Software de Código Abierto: Contribuyo a proyectos en GitHub, colaborando con otros
                desarrolladores para mejorar herramientas y librerías populares.
            </li>
            <li class="item">
                Deportes al Aire Libre: Disfruto del senderismo y el ciclismo de montaña, actividades que practico
                regularmente para mantener un equilibrio entre el trabajo y la vida personal.
            </li>
            <li class="item">
                Tecnología de Innovación: Me apasiona explorar nuevas tendencias tecnológicas como la inteligencia
                artificial y el desarrollo de aplicaciones móviles.
            </li>
            <li class="item">
                Fotografía: Practico la fotografía como un hobby, lo que me ayuda a mantener una perspectiva creativa
                tanto en mi vida profesional como personal.
            </li>
        </ul>
    </div> -->
</template>

<style scoped>
.intereses-contenedor {
    display: flex;
    margin: 0 auto;
    justify-content: center;
    border: 1px solid#dda15e;
    border-radius: 8px;
    padding: 2em 0; 
    box-shadow: 0 0 5px 3px #283618a5;

}

.contenedor-lista {
    display: flex;
    flex-flow: column;
    gap:30px;
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
    
    
    
    
}

.item {
    padding: 5px 10px;
    border: 1px solid #606c38;
    border-radius: 8px;
    background-color: #606c38;
    text-transform: uppercase;
    text-align: center;


}

@media screen and (max-width:768px) {
    .contenedor-lista{
        flex-flow: row wrap;
        margin: 0;
        padding: 0;

    }
}
</style>