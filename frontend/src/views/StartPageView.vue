<script setup>
import ScrollingItems from '@/components/ScrollingItems.vue';
import StartHeroSpawner from "@/components/StartHeroSpawner.vue";
import { useRouter } from 'vue-router';
import { useHeroStore } from "@/stores/HeroStore.js";

const router = useRouter();
const heroStore = useHeroStore();

const continueGame = () => {
  heroStore.loadHeroData();

  if (heroStore.HeroGroup1.length > 0) {
    router.push({ name: 'MainPage' });
  } else {
    alert("No existing game found. Please start a new game.");
  }
};

function goToNewTownName() {
  heroStore.clearHeroData();
  router.push({ name: 'SignUp' });
}
</script>

<template>
  <div class="welcome-container">
    <ScrollingItems />
    <h1 class="title">Welcome to MayoRPG</h1>
    <div class="button-container">
      <button @click="goToNewTownName" class="player-button">New Player</button>
      <button @click="continueGame" class="player-button">Returning Player</button>
    </div>
    <StartHeroSpawner />
  </div>
</template>

<style scoped>
.welcome-container {
  font-family: 'Press Start 2P', cursive;
  position: relative;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
  top: 4vh;
}

.title {
  background: linear-gradient(45deg, #3e312d, #6d5648);
  padding: 10px 30px;
  border: 2px solid black;
  border-radius: 10px;
  font-size: 3em;
  text-shadow: 2px 2px 4px #000000;
  position: relative;
  z-index: 1;
  color: #f8e8c8;
  margin-bottom: 40px;
  margin-top: 200px;
  animation: pulse 4s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

.button-container {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.player-button {
  background-color: #3e312d;
  color: #f8e8c8;
  font-size: 1rem;
  padding: 10px 30px;
  border: 2px solid black;
  border-radius: 10px;
  cursor: pointer;
  width: 200px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.player-button:hover {
  background-color: #6d5648;
  transform: scale(1.1);
}
</style>