<script setup>
import { ref, onMounted } from 'vue';

const heroes = ref([]);
const NUM_HEROES_TO_DISPLAY = 15;

onMounted(() => {
  const images = import.meta.glob('@/assets/hero-gifs/*.gif');
  const allHeroes = [];
  const imagePromises = [];

  for (const path in images) {
    imagePromises.push(images[path]().then((mod) => mod.default));
  }

  Promise.all(imagePromises).then((loadedHeroes) => {
    allHeroes.push(...loadedHeroes);
    heroes.value = getRandomSubset(allHeroes, NUM_HEROES_TO_DISPLAY);
  });
});

function getRandomSubset(arr, size) {
  const shuffled = arr.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, size);
}
</script>

<template>
  <div class="hero-spawner">
    <img v-for="(hero, index) in heroes" :key="index" :src="hero" alt="hero" class="hero-image"/>
  </div>
</template>

<style scoped>
.hero-spawner {
  position: fixed;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 5px;
}

.hero-image {
  width: 100px;
  height: auto;
  transition: transform 0.3s ease;
}

.hero-image:hover {
  transform: translateY(-150px);
}
</style>