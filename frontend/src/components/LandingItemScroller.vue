<script setup>
import { ref, onMounted, computed } from 'vue';

const props = defineProps({
  speed: {
    type: Number,
    default: 20,
  },
});

const items = ref([]);
const loading = ref(true);
const NUM_ITEMS_TO_DISPLAY = 20;
const MAX_ITEMS = 999;

const scrollSpeed = computed(() => {
  return `${props.speed}s`;
});

function getRandomNumbers(count, max) {
  const numbers = new Set();
  while (numbers.size < count) {
    const randomNum = Math.floor(Math.random() * (max + 1));
    numbers.add(randomNum);
  }
  return Array.from(numbers);
}

onMounted(async () => {
  const randomNumbers = getRandomNumbers(NUM_ITEMS_TO_DISPLAY, MAX_ITEMS);
  const formattedNumbers = randomNumbers.map(num => String(num).padStart(3, '0'));

  const imagePromises = formattedNumbers.map(num =>
    import(`@/assets/items/tile${num}.png`).then(mod => mod.default)
  );

  items.value = await Promise.all(imagePromises);
  loading.value = false;
});
</script>

<template>
  <div class="random-item-scroller left" :style="{ '--scroll-speed': scrollSpeed }">
    <div v-if="loading" class="spinner-container">
      <div class="spinner"></div>
      <div class="loading-text">Loading...</div>
    </div>
    <div v-else class="scroller-content">
      <div
        class="item"
        v-for="(item, index) in items"
        :key="`left-${index}`"
      >
        <img :src="item" alt="Item Image" class="scroller-image" loading="lazy" />
      </div>
      <div
        class="item"
        v-for="(item, index) in items"
        :key="`left-clone-${index}`"
      >
        <img :src="item" alt="Item Image" class="scroller-image" loading="lazy" />
      </div>
    </div>
  </div>

  <div class="random-item-scroller right" :style="{ '--scroll-speed': scrollSpeed }">
    <div v-if="loading" class="spinner-container">
      <div class="spinner"></div>
      <div class="loading-text">Loading...</div>
    </div>
    <div v-else class="scroller-content reverse">
      <div
        class="item"
        v-for="(item, index) in items"
        :key="`right-${index}`"
      >
        <img :src="item" alt="Item Image" class="scroller-image" loading="lazy" />
      </div>
      <div
        class="item"
        v-for="(item, index) in items"
        :key="`right-clone-${index}`"
      >
        <img :src="item" alt="Item Image" class="scroller-image" loading="lazy" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.random-item-scroller {
  position: fixed;
  top: 0;
  bottom: 0;
  width: 120px;
  overflow: hidden;
  z-index: 500;
  height: 100vh;
}

.random-item-scroller.left {
  left: 0;
}

.random-item-scroller.right {
  right: 0;
}

.spinner-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.spinner {
  border: 8px solid #f3f3f3; /* Light grey */
  border-top: 8px solid #f59e0b; /* Yellow */
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spin 1.5s linear infinite;
}

.loading-text {
  margin-top: 10px;
  color: #f59e0b;
  font-size: 1rem;
}

.scroller-content {
  display: flex;
  flex-direction: column;
  height: 200%; /* To accommodate duplicated items */
  animation: scroll-up var(--scroll-speed) linear infinite;
}

.scroller-content.reverse {
  animation: scroll-up var(--scroll-speed) linear infinite reverse;
}

.item {
  flex-shrink: 0;
}

.scroller-image {
  width: 100%;
  height: auto;
  margin-bottom: 1rem; /* Space between images */
  object-fit: contain;
  transition: transform 0.3s ease;
}

.scroller-image:hover {
  transform: scale(1.1);
}

/* Define CSS variable for scroll speed */
:root {
  --scroll-speed: 40s;
}

@keyframes scroll-up {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(-50%);
  }
}

/* Spinner Animation */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
