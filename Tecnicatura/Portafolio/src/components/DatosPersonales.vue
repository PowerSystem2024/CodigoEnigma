<script setup>
import linkedin from '../assets/icons/ri--linkedin-line.svg'
import github from '../assets/icons/ri--github-line.svg'
import instagram from '../assets/icons/ri--instagram-line.svg'
import twitter from '../assets/icons/ri--twitter-x-fill.svg'

const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin, url: '' },
  { id: 2, name: 'github', src: github, url: '' },
  { id: 3, name: 'Instagram', src: instagram, url: '' },
  { id: 4, name: 'twitter', src: twitter, url: '' },
]
</script>

<template>
  <section class="datos-personales">
    <article class="title">
        <h1>&lt;Código Enigma/&gt;</h1>
      <p>
        Eliana Dominguez <b>|</b> Arón Rojas <b>|</b> Francisco Elías <b>|</b> Rocío Aguirre Cerullo <b>|</b>
        Dilan Ramos <b>|</b> Agustín Colombo <b>|</b> Juan Cruz Dicalbo.
      </p>
    </article>

    <article class="redes">
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url"
            ><img
              class="icon-redsocial"
              :src="red.src"
              width="35rem"
              :alt="red.name"
          /></a>
        </li>
      </ul>

      <button>Descargar CV</button>
    </article>
  </section>
</template>

<style scoped>
.datos-personales {
  padding: 7rem 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  text-align: center;
}

.title {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.redes {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
}

ul {
  list-style: none;
  display: flex;
  gap: 2rem;
}

li {
  padding: 0.5rem;
  border-radius: 50px;
  border: 1px solid var(--white-quaternary);
  display: flex;
  align-items: center;
}

li:hover {
  background-color: var(--hover-color-opacity);
}

a {
  display: flex;
  align-items: center;
}

.icon-redsocial {
  width: 1.5rem;
}

span {
  font-weight: bold;
}

button {
  padding: 0.5rem 1rem;
  border-radius: 50px;
  border: 1px solid var(--white-quaternary);
  background-color: transparent;
  color: var(--white-primary);
  font-weight: 600;
  cursor: pointer;
  font-size: 1rem;
}

button:hover {
  background-color: var(--white-primary);
  color: var(--black-primary);
}
</style>
