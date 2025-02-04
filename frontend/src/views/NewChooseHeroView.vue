<script setup>
import { computed, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import ChooseHeroCard from "@/components/ChooseHeroCard.vue";
import { useHeroStore } from "@/stores/HeroStore.js";
import StartHeroSpawner from "@/components/StartHeroSpawner.vue";
import ScrollingItems from "@/components/ScrollingItems.vue";

const router = useRouter();
const heroStore = useHeroStore();

const heroes = computed(() => heroStore.heroes);
const currentIndex = ref(0);

const selectedHero = computed(() => {
  return heroes.value.length > 0 ? heroes.value[currentIndex.value] : null;
});

function adjustIndex(index) {
  const count = heroes.value.length;
  if (count === 0) return 0;
  return ((index % count) + count) % count;
}

const displayedHeroes = computed(() => {
  const count = heroes.value.length;
  if (count === 0) return [];
  const prevIndex = adjustIndex(currentIndex.value - 1);
  const nextIndex = adjustIndex(currentIndex.value + 1);
  return [
    heroes.value[prevIndex],
    heroes.value[currentIndex.value],
    heroes.value[nextIndex]
  ];
});

function selectHero(hero) {
  if (hero) {
    heroStore.selectHero(hero.name);
  }
}

function moveLeft() {
  currentIndex.value = adjustIndex(currentIndex.value - 1);
}

function moveRight() {
  currentIndex.value = adjustIndex(currentIndex.value + 1);
}

function navigateToDashboard() {
  if (selectedHero.value) {
    selectHero(selectedHero.value);
  }
  router.push({ name: 'ChooseHeroClass' });
}

onMounted(() => {
  heroStore.loadInitialHeroData();
});
</script>


<template>
  <div class="hero-selection">
    <ScrollingItems />
    <h1 class="title">Choose Your Hero</h1>
    <div class="navigation-container">
      <button @click="moveLeft"> <<< </button>
      <div class="card-container">
        <ChooseHeroCard
          v-for="(hero, index) in displayedHeroes"
          :key="hero.name"
          :hero="hero"
          :is-selected="index === 1"
          @select="() => selectHero(hero)"
          :class="{ 'is-large': index === 1 }"
        />
      </div>
      <button @click="moveRight"> >>> </button>
    </div>
    <button class="continue-button" @click="navigateToDashboard">Continue</button>
  </div>
  <StartHeroSpawner />
</template>


<style scoped>
.title {
  color: #f8facc;
  text-align: center;
  font-size: 3rem;
  margin-bottom: 1rem;
  font-family: 'Press Start 2P', cursive;
  position: relative;
  display: inline-block;
  background-color: #2c3e50;
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
  border-radius: 10px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
  padding: 10px 20px;
  box-shadow: 8px 8px 0 rgba(0, 0, 0, 0.4);
}

.hero-selection {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 95vh;
  padding: 20px;
  position: relative;
  z-index: 1;
}

.navigation-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-bottom: 2rem;
}

.card-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  overflow: hidden;
  max-width: 80%;
  z-index: 1;
}

.is-large {
  transform: scale(1.1);
  margin: 40px;
  cursor: pointer;
  border: 4px solid #f8facc;
}

button {
  padding: 1.5rem 3rem;
  font-size: 1.5rem;
  color: #f8facc;
  border: none;
  border-radius: 8px;
  margin: 40px;
  cursor: pointer;
  font-family: 'Press Start 2P', cursive;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
  background-color: #2c3e50;
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
}

button:first-child {
  left: 10px;
}

button:last-child {
  right: 10px;
}

button:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
}

.continue-button {
  background-color: #3e312d;
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
  color: #f8facc;
  border: 2px solid #f8facc;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  transition: background-color 0.3s, box-shadow 0.3s;
  z-index: 1;
}

.continue-button:hover {
  background-color: #6d5648;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
}
</style>