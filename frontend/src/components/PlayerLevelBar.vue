<script setup>
import { computed } from 'vue'

const experiencePercentage = computed(() => 35)
const experienceRatio = computed(() => '35 / 100')
const currentLevel = computed(() => 1)
</script>

<template>
  <div class="level-container">
    <span class="level-label">Level: {{ currentLevel }}</span>
    <div class="progress-container">
      <div class="progress-bar" :style="{ width: experiencePercentage + '%' }">
        <span class="progress-text">{{ experienceRatio }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.level-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
  margin: 0.5rem 0;
}

.level-label {
  margin-bottom: 4px;
  font-size: 1rem;
  text-shadow: 1px 1px 2px #000;
}

.progress-container {
  position: relative;
  width: 53rem;
  height: 2rem;
  background-color: #3a2518;
  border: 2px solid #c2a368;
  border-radius: 4px;
  box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.7);
}

.progress-bar {
  height: 100%;
  background: linear-gradient(
    90deg,
    rgba(166, 95, 61, 1) 0%,
    rgba(194, 163, 104, 1) 100%
  );
  border-radius: 2px;
  transition: width 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-text {
  text-shadow: 1px 1px 2px #000;
  pointer-events: none;
}
</style>
