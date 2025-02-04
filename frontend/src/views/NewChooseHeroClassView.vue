<script setup>
import ChooseClassCard from "@/components/ChooseClassCard.vue";
import { useHeroStore } from "@/stores/HeroStore.js";
import { useRouter } from 'vue-router';
import {computed} from "vue";
import ScrollingItems from "@/components/ScrollingItems.vue";
import StartHeroSpawner from "@/components/StartHeroSpawner.vue";

const router = useRouter();
const heroStore = useHeroStore();

const hero = computed(() => heroStore.selectedHero);


function selectHero(hero) {
  heroStore.confirmHeroSelection(hero.heroGroup);
}

const Continue = () => {
  if (!hero.value) {
    alert("No hero selected. Please select a hero.");
    return;
  }
  selectHero(hero.value);
  router.push({ name: 'MainPage' });
};

const Back = () => {
  router.push({ name: 'ChooseHero' });
};
</script>


<template>
  <div class="centered-container">
    <ScrollingItems />
    <div class="cards-container" v-if="hero">
      <div class="choose-class">
        <h1 class="title">Choose Your Class</h1>
        <ChooseClassCard :hero="hero" class="choose-class-card" @click="Continue" />
      </div>
    </div>
    <div v-else>
      <p>Loading hero data or no hero selected...</p>
    </div>
    <div class="button-container">
      <button @click="Back">Back</button>
    </div>
  </div>
  <StartHeroSpawner />
</template>


<style scoped>
.title {
  color: #fff;
  text-align: center;
  font-size: 1.5rem;
  margin-top: 0;
  margin-bottom: .5rem;
  margin-left: 1rem;
  font-family: 'Press Start 2P', cursive;
  position: relative;
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
  border-radius: 10px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
  padding: 10px 20px;
  box-shadow: 8px 8px 0 rgba(0, 0, 0, 0.4);
}

.centered-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 75vh;
  position: relative;
  padding: 20px;
}

.cards-container {
  display: flex;
  gap: 20px;
  width: 65%;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  z-index: 1;
}

.hero-stats-card, .choose-class {
  display: flex;
  flex-direction: column;
}

.button-container {
  display: flex;
  justify-content: flex-end;
  width: 80%;
}

button {
  padding: 1.5rem 3rem;
  font-size: 1.5rem;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-family: 'Press Start 2P', cursive;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
  flex: none;
  margin: 0 20px;
}

button:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
}
</style>
