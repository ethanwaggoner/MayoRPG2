<script setup>
import {onMounted, ref} from 'vue';

const items = ref([]);
const loading = ref(true);
const NUM_ITEMS_TO_DISPLAY = 20;
const MAX_ITEMS = 1000;

onMounted(async () => {
  const randomNumbers = getRandomNumbers(NUM_ITEMS_TO_DISPLAY, MAX_ITEMS);
  const imagePromises = randomNumbers.map(num => import(`@/assets/items/tile${num}.png`).then(mod => mod.default));

  items.value = await Promise.all(imagePromises);
  loading.value = false;
});

function getRandomNumbers(count, max) {
  const numbers = new Set();
  while (numbers.size < count) {
    const randomNum = String(Math.floor(Math.random() * max) + 1).padStart(3, '0');
    numbers.add(randomNum);
  }
  return Array.from(numbers);
}
</script>

<template>
  <div class="item-scroller">
    <div v-if="loading" class="spinner-container">
      <div class="spinner"></div>
      <div class="loading-text">Loading...</div>
    </div>
    <div v-else class="column" v-for="n in 8" :key="n">
      <div class="item" v-for="item in items" :key="item">
        <img :src="item" alt="item"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.item-scroller {
  border: black 2px solid;
  border-radius: 50%;
  background: linear-gradient(45deg, #6d5648, #3e312d);
  width: 55%;
  height: 650px;
  display: flex;
  justify-content: center;
  overflow: hidden;
  position: absolute;
  z-index: 0;
  opacity: .7;
}

.column {
  flex: 1;
  display: flex;
  flex-direction: column;
  animation: scroll 30s linear infinite;
  margin: 0 20px;
}

.item {
  flex-shrink: 0;
}

img {
  width: 80px;
  height: 80px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

img:hover {
  transform: scale(1.1);
}

.spinner-container {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  height: 100%;
  width: 100%;
}

.spinner {
  border: 16px solid black;
  border-top: 16px solid #f8e8c8;
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
}

.loading-text {
  margin-top: 20px;
  font-size: 1.5em;
  color: #f8e8c8;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes scroll {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-100%);
  }
}
</style>